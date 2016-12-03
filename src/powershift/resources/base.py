import json
import keyword
import sys
import re
import os

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')

def convert_camel_to_snake(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()

def map_property_name(name):
    if keyword.iskeyword(name):
        name = name + '_'
    return convert_camel_to_snake(name)

def map_properties(properties):
    return {map_property_name(name): value
            for (name, value) in properties.items()}

_resource_object_types = {}

def registered_resource_types():
    return _resource_object_types

def register_resource(cls):
    _resource_object_types[cls.__kind__] = cls
    return cls

class Resource(object):

    __kind__ = None

    __fields__ = {}

    __types__ = {}

    __required__ = set()

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        if self.__kind__:
            _translate_properties(self)
            _validate_properties(self, kwargs)

    def __getattr__(self, name):
        return self.__dict__[name]

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getitem__(self, name):
        return self.__dict__[name]

    def __contains__(self, name):
        return name in self.__dict__

    def __setitem__(self, name, value):
        self.__dict__[name] = value

    def __iter__(self):
        return iter(self.__dict__)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, ', '.join(
                ['%s=%r' % (k, v) for k, v in self.__dict__.items()]))

    def __json__(self):
        data = {}

        for name, value in self.__dict__.items():
            # If property is a list but is not a required
            # then do not output it in the JSON.

            if name not in self.__required__:
                if isinstance(value, list) and not value:
                    continue

            # Map back to the original property name.

            name = self.__fields__.get(name, name)
            data[name] = value

        return data

@register_resource
class List(Resource):

    __kind__ = 'v1.List'

    __fields__ = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'items': 'items',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    def __init__(self, **_kwargs_):

        self.kind = 'List'

        self.items = []

        super().__init__(**_kwargs_)

def _translate_properties(obj):
    # Go through the properties of a resource and convert to a specific
    # type if one has been associated with that property.

    for name, value in list(vars(obj).items()):
        if name in obj.__types__:
            if isinstance(value, list):
                # In the case of a list of values for a property,
                # need to convert each one to the appropriate
                # type.

                new_items = []

                cls = _resource_object_types[obj.__types__[name]]

                for item in value:
                    if isinstance(item, Resource):
                        new_items.append(cls(**map_properties(vars(item))))
                    else:
                        new_items.append(item)

                setattr(obj, name, new_items)

            elif isinstance(value, Resource):
                undef = object()
                value = getattr(obj, name, undef)

                cls = _resource_object_types[obj.__types__[name]]

                setattr(obj, name, cls(**map_properties(vars(value))))

_ignore_properties = {
    'runtime.RawExtension': set(['*']),
    'v1.Container': set(['capabilities']), # Error in openshift default templates.
    'v1.Route': set(['id']), # Error in openshift default templates.
}

_bool_tokens = ('1', 'true', 'enabled', 'on')

def _validate_properties(obj, kwargs):
    # Validate that not being supplied optional properties we do not
    # know anything about. Certain types can contain variable opaque
    # data so we need to ignore those. Others may have specific
    # properties which should be ignored as schema data provides
    # incorrect information about them. For now this generates an
    # assertion failure.

    validate = (os.environ.get('OPENSHIFT_API_VALIDATE', 'false').lower()
            in _bool_tokens)

    if '*' in _ignore_properties.get(obj.__kind__, set()):
        return

    for name in kwargs.keys():
        if name in _ignore_properties.get(obj.__kind__, set()):
            continue

        if validate:
            assert name in obj.__fields__, '%s %s' % (obj.__kind__, name)

def _default_encoder(obj):
    if isinstance(obj, Resource):
        return obj.__json__()

    raise TypeError('cannot encode to JSON, unknown type')

def _object_decoder(items):
    # Does the resource map to a defined type. If it does we
    # need to map any property names and then create the type.

    if 'kind' in items and 'apiVersion' in items:
        type_name = '%s.%s' % (items['apiVersion'], items['kind'])

        if type_name in _resource_object_types:
            return _resource_object_types[type_name](**map_properties(items))

    # Where no defined type, we use the original property names.

    return Resource(**items)

def loads(data):
    return json.loads(data, object_hook=_object_decoder)

def load(path=None):
    if path is None:
        return loads(sys.stdin.read())

    with open(path) as fp:
        return loads(fp.read())

def dumps(obj, indent=None, sort_keys=False):
    return json.dumps(obj, default=_default_encoder, indent=indent,
            sort_keys=sort_keys)

def dump(obj, path=None, indent=None, sort_keys=False):
    if path is None:
        sys.stdout.write(dumps(obj, indent, sort_keys))
        return

    with open(path, 'w') as fp:
        fp.write(dumps(obj))
