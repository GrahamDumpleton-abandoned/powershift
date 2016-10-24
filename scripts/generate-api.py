import json
import keyword
import textwrap
import operator
import re

prologue_template = """
# XXX This code file has been automatically generated. Do not edit it.

import requests as _requests_

from .base import EndPoint, register_endpoint
from .. import resources as _resources_
"""

def generate_prologue():
    print(prologue_template)

_endpoint_param_overrides = [
     ('/api/v1/namespaces/{name}',  {"name": "namespace"}),
     ('/api/v1/watch/namespaces/{name}', {"name": "namespace"}),
]

_endpoint_ignore_endpoints = [
    '/api/v1/watch/',
    '/oapi/v1/watch/',
]

def fixup_url_path(path):
    for prefix, mapping in _endpoint_param_overrides:
        if path.startswith(prefix):
            for old, new in mapping.items():
                path = path.replace('{%s}' % old, '{%s}' % new)
    return path

def map_url_path(path):
    path = path.lstrip('/')
    path = path.replace('{', '')
    path = path.replace('}', '')
    path = path.replace('/', '_')
    return path

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')

def convert_camel_to_snake(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()

def map_param_name(path, name):
    for prefix, mapping in _endpoint_param_overrides:
        if path.startswith(prefix):
            name = mapping.get(name, name)
    if keyword.iskeyword(name):
        name = name + '_'
    return convert_camel_to_snake(name)

# A class definition is generated for each endpoint from the api definitions
# in the schema data. 

def generate_endpoints(apis):
    endpoints = {}

    for api in apis:
        path = api['path']
        path = fixup_url_path(path)
        endpoints[path] = {}

    for path in endpoints.keys():
        if '{' in path:
            parts = path.split('/')
            prefix = []
            for part in parts:
                if part.startswith('{'):
                    parent = '/'.join(prefix)
                    if parent in endpoints:
                        endpoints[parent].setdefault(part, []).append(path)
                else:
                    prefix.append(part)

    for api in sorted(apis, key=operator.itemgetter('path')):
        orig_path = api['path']

        ignore_endpoint = False

        for ignore in _endpoint_ignore_endpoints:
            if orig_path.startswith(ignore):
                ignore_endpoint = True
                break

        if ignore_endpoint:
            continue

        print()

        path = fixup_url_path(orig_path)

        class_name = map_url_path(path)

        print('@register_endpoint')
        print('class EndPoint_%s(EndPoint):' % class_name)

        print()

        print('    path = %r' % path)

        path_params = []
        for part in path.split('/')[::-1]:
            if part.startswith('{'):
                part = part.lstrip('{').rstrip('}')
                mapped_param = map_param_name(orig_path, part)
                path_params.append(mapped_param)
            else:
                break
        path_params.reverse()

        for operation in api['operations']:
            method = operation['method'].lower()

            print()
            print('    _%s_type_ = %r' % (method, operation['type']))

            print()
            print('    _%s_ = {}' % method)

            required_params = list(path_params)

            query_params = []
            body_params = []

            for param in operation['parameters']:
                mapped_param = map_param_name(orig_path, param['name'])
                print('    _%s_[%r] = {' % (method, mapped_param))
                print('        %r: %r,' % ('name', param['name'])) 
                print('        %r: %r,' % ('type', param['type'])) 
                print('        %r: %r,' % ('param_type', param['paramType'])) 
                print('        %r: %r,' % ('required', param['required'])) 
                print('    }')

                if param['required']:
                    if param['paramType'] == 'query':
                        query_params.append(mapped_param)
                    elif param['paramType'] == 'body':
                        body_params.append(mapped_param)

            print()

            required_params.extend(query_params)
            required_params.extend(body_params)

            print('    def %s(self' % method, end='')
            if required_params:
                print(', *', end='')
            for name in required_params:
                print(', %s' % name, end='')
            print(', **_kwargs_):')

            print('        _params_ = dict(self.params)')

            for param in path_params:
                print('        _params_[%r] = %s' % (param, param))

            print('        _path_ = self.path.format(**_params_)')

            for param in query_params:
                print('        _params_[%r] = %s' % (map_param_name(orig_path, param), param))

            print('        for _name_, _param_ in self._%s_.items():' % method)
            print('            if _name_ in _kwargs_:')
            print('                _params_[_param_[\'name\']] = _kwargs_[_name_]')

            if body_params:
                print('        _body_ = %s' % body_params[0])
            else:
                print('        _body_ = None')

            print('        _url_ = \'https://%s%s\' % (self.client.host, _path_)')

            print('        _headers_ = { \'Authorization\': \'Bearer %s\' % self.client.token }')

            print('        _response_ = _requests_.%s(_url_, headers=_headers_,' % method)
            print('                params=_params_, verify=self.client.verify)')

            print('        _result_ = _resources_.loads(_response_.text)')

            print('        if _result_.__kind__ != self._%s_type_:' % method)
            print('            raise Exception(str(_result_))')

            print('        return _result_')

        if path in list(endpoints.keys()):
            if endpoints[path]:
                assert len(endpoints[path].keys()) == 1, endpoints[path]

                part, children = endpoints[path].popitem()
                name = part.lstrip('{').rstrip('}')
                child = '%s/%s' % (path, part)

                print()
                print('    def __call__(self, *, %s):' % name)
                print('        params = dict(self.params)')
                print('        params[%r] = %s' % (name, name))

                if child in endpoints:
                    class_name = map_url_path(child)
                    print('        return EndPoint_%s(self.client, **params)' % class_name)
                else:
                    print('        return EndPoint(self.client, %r, **params)' % child)

generate_prologue()

schema = json.loads(open('schemas/openshift-v1-api.json').read())
generate_endpoints(schema['apis'])

schema = json.loads(open('schemas/openshift-v1-oapi.json').read())
generate_endpoints(schema['apis'])
