import json
import keyword
import textwrap
import re

prologue_template = """
# XXX This code file has been automatically generated. Do not edit it.

from .base import Resource, register_model
"""

def generate_prologue():
    print(prologue_template)

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')

def convert_camel_to_snake(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()

def map_property_name(name):
    if keyword.iskeyword(name):
        name = name + '_'
    return convert_camel_to_snake(name)

# The schema data appears to be providing incorrect data about what
# fields are required. Appears that the schema is really tracking what
# properties the server will always fill in with data, rather than
# properly indicating what should be provided. Override these for now.

_required_property_overrides = {
    'v1.BuildConfig': { 'status': False },
    'v1.BuildSource': { 'secrets': False },
    'v1.DeploymentConfig': { 'status': False },
    'v1.DeploymentConfigSpec': { 'test': False, 'strategy': False },
    'v1.ImageStream': { 'spec': False },
    'v1.Route': { 'status': False },
    'v1.RouteSpec': { 'host': False },
    'v1.RouteTargetReference': { 'weight': False },
    'v1.TagReference': { 'annotations': False, 'generation': False }
}

def required_properties(type_name, definition):
    required = definition.get('required', [])
    new_required = []

    overrides = _required_property_overrides.get(type_name, {})

    for name, flag in overrides.items():
        if flag == True:
            new_required.append(name)

    for name in required:
        if overrides.get(name, True):
            new_required.append(name)

    return sorted(new_required)

# The schema data in some cases provides the incorrect type for a
# property. Override these for now.

_property_type_overrides = {
    'v1.Capabilities' : { 'drop': 'type:string' },
    'v1.PersistentVolumeClaimSpec' : { 'accessModes': 'type:string' }
}

# A class definition is generated for each resource from the model in
# the schema data. These will all be added to a global registry so that
# when decoding JSON definition can automatically map to the correct type.

def generate_resources(models):
    types = []

    for type_name, definition in models:
        print()

        class_name = '%s' % type_name.replace('.', '_').replace('*', '')

        types.append(class_name)

        print('@register_model')
        print('class %s(Resource):' % class_name)

        print()

        if definition.get('description'):
            print('    """%s"""' % '\n'.join(textwrap.wrap(
                    definition['description'], width=70, initial_indent='',
                    subsequent_indent='    ')))
            print()

        print('    __kind__ = %s' % repr(type_name))

        print()

        print('    __fields__ = {')

        for property_name in definition['properties'].keys():
            print('        %r: %r,' % (map_property_name(property_name),
                    property_name))

        print('    }')

        print()

        refs = {}

        for property_name, details in definition['properties'].items():
            if '$ref' in details:
                override = _property_type_overrides.get(type_name, {}).get(
                        property_name, None)

                if override:
                    if override.startswith('$ref:'):
                        refs[property_name] = override.split(':')[1]
                    elif override.startswith('type:'):
                        pass
                else:
                    refs[property_name] = details['$ref']

            elif ('type' in details and details['type'] == 'array' and
                    '$ref' in details['items']):

                override = _property_type_overrides.get(type_name, {}).get(
                        property_name, None)

                if override:
                    if override.startswith('$ref:'):
                        refs[property_name] = override.split(':')[1]
                    elif override.startswith('type:'):
                        pass
                else:
                    refs[property_name] = details['items']['$ref']

        print('    __types__ = {')

        for property_name, type_name in refs.items():
            print('        %r: %r,' % (map_property_name(property_name),
                    type_name))

        print('    }')

        print()

        required = required_properties(type_name, definition)

        if required:
            print('    __required__ = set([')
            for property_name in required:
                print('        %r,' % map_property_name(property_name))
            print('    ])')
            
        else:
            print('    __required__ = set()')

        print()

        for property_name, details in definition['properties'].items():
            property_type = details.get('type')

            if not property_type:
                property_type = details.get('$ref', '???')

            print('    %s = None # %s' % (map_property_name(property_name),
                    property_type), end='')

            if property_name in required:
                print(' (required)')
            else:
                print()

        print()

        print('    def __init__(self', end='')

        if required:
            print(', *', end='')

            for required_name in required:
                print(', %s' % map_property_name(required_name), end='')

        print(', **_kwargs_):')

        for property_name, details in definition['properties'].items():
            if property_name not in required:
                if details.get('type') == 'array':
                    print('        self.%s = []' % map_property_name(property_name))

        if 'kind' in definition['properties']:
            print()
            print('        self.kind = %s' % repr(type_name.split('.')[-1]))

        if required:
            print()

            for required_name in required:
                print('        self.%s = %s' % (map_property_name(
                        required_name), map_property_name(required_name)))

        print()

        print('        super().__init__(**_kwargs_)')

    print('__all__ = %r' % types)

generate_prologue()

schema = json.loads(open('schemas/openshift-v1-api.json').read())
generate_resources(schema['models'].items())

schema = json.loads(open('schemas/openshift-v1-oapi.json').read())
generate_resources(schema['models'].items())
