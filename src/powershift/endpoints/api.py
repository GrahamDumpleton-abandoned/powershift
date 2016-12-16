
# XXX This code file has been automatically generated. Do not edit it.

import requests as _requests_

from .base import EndPoint, register_endpoint
from .. import resources as _resources_


@register_endpoint
class EndPoint_api_v1(EndPoint):

    path = '/api/v1'

    _get_type_ = 'unversioned.APIResourceList'

    _get_ = {}

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_bindings(EndPoint):

    path = '/api/v1/bindings'

    _post_type_ = 'v1.Binding'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Binding',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_componentstatuses(EndPoint):

    path = '/api/v1/componentstatuses'

    _get_type_ = 'v1.ComponentStatusList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_api_v1_componentstatuses_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_api_v1_componentstatuses_name(EndPoint):

    path = '/api/v1/componentstatuses/{name}'

    _get_type_ = 'v1.ComponentStatus'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_configmaps(EndPoint):

    path = '/api/v1/configmaps'

    _get_type_ = 'v1.ConfigMapList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ConfigMap'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ConfigMap',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_endpoints(EndPoint):

    path = '/api/v1/endpoints'

    _get_type_ = 'v1.EndpointsList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Endpoints'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Endpoints',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_events(EndPoint):

    path = '/api/v1/events'

    _get_type_ = 'v1.EventList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Event'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Event',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_limitranges(EndPoint):

    path = '/api/v1/limitranges'

    _get_type_ = 'v1.LimitRangeList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.LimitRange'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.LimitRange',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces(EndPoint):

    path = '/api/v1/namespaces'

    _get_type_ = 'v1.NamespaceList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Namespace'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Namespace',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, namespace):
        params = dict(self.params)
        params['namespace'] = namespace
        return EndPoint_api_v1_namespaces_namespace(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_bindings(EndPoint):

    path = '/api/v1/namespaces/{namespace}/bindings'

    _post_type_ = 'v1.Binding'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Binding',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_configmaps(EndPoint):

    path = '/api/v1/namespaces/{namespace}/configmaps'

    _get_type_ = 'v1.ConfigMapList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ConfigMap'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ConfigMap',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_configmaps_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/configmaps/{name}'

    _get_type_ = 'v1.ConfigMap'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ConfigMap'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ConfigMap',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ConfigMap'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_endpoints(EndPoint):

    path = '/api/v1/namespaces/{namespace}/endpoints'

    _get_type_ = 'v1.EndpointsList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Endpoints'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Endpoints',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_endpoints_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/endpoints/{name}'

    _get_type_ = 'v1.Endpoints'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Endpoints'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Endpoints',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Endpoints'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_events(EndPoint):

    path = '/api/v1/namespaces/{namespace}/events'

    _get_type_ = 'v1.EventList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Event'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Event',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_events_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/events/{name}'

    _get_type_ = 'v1.Event'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Event'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Event',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Event'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_limitranges(EndPoint):

    path = '/api/v1/namespaces/{namespace}/limitranges'

    _get_type_ = 'v1.LimitRangeList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.LimitRange'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.LimitRange',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_limitranges_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/limitranges/{name}'

    _get_type_ = 'v1.LimitRange'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.LimitRange'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.LimitRange',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.LimitRange'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_persistentvolumeclaims(EndPoint):

    path = '/api/v1/namespaces/{namespace}/persistentvolumeclaims'

    _get_type_ = 'v1.PersistentVolumeClaimList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.PersistentVolumeClaim'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.PersistentVolumeClaim',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_persistentvolumeclaims_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}'

    _get_type_ = 'v1.PersistentVolumeClaim'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.PersistentVolumeClaim'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.PersistentVolumeClaim',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.PersistentVolumeClaim'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_persistentvolumeclaims_name_status(EndPoint):

    path = '/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status'

    _get_type_ = 'v1.PersistentVolumeClaim'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.PersistentVolumeClaim'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.PersistentVolumeClaim',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.PersistentVolumeClaim'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods'

    _get_type_ = 'v1.PodList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Pod'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Pod',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods/{name}'

    _get_type_ = 'v1.Pod'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Pod'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Pod',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Pod'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods_name_attach(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods/{name}/attach'

    _get_type_ = 'string'

    _get_ = {}
    _get_['stdin'] = {
        'name': 'stdin',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['stdout'] = {
        'name': 'stdout',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['stderr'] = {
        'name': 'stderr',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['tty'] = {
        'name': 'tty',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['container'] = {
        'name': 'container',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['stdin'] = {
        'name': 'stdin',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _post_['stdout'] = {
        'name': 'stdout',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _post_['stderr'] = {
        'name': 'stderr',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _post_['tty'] = {
        'name': 'tty',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _post_['container'] = {
        'name': 'container',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods_name_binding(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods/{name}/binding'

    _post_type_ = 'v1.Binding'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Binding',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods_name_eviction(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods/{name}/eviction'

    _post_type_ = 'v1alpha1.Eviction'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1alpha1.Eviction',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods_name_exec(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods/{name}/exec'

    _get_type_ = 'string'

    _get_ = {}
    _get_['stdin'] = {
        'name': 'stdin',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['stdout'] = {
        'name': 'stdout',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['stderr'] = {
        'name': 'stderr',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['tty'] = {
        'name': 'tty',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['container'] = {
        'name': 'container',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['command'] = {
        'name': 'command',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['stdin'] = {
        'name': 'stdin',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _post_['stdout'] = {
        'name': 'stdout',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _post_['stderr'] = {
        'name': 'stderr',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _post_['tty'] = {
        'name': 'tty',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _post_['container'] = {
        'name': 'container',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['command'] = {
        'name': 'command',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods_name_log(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods/{name}/log'

    _get_type_ = 'v1.Pod'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['container'] = {
        'name': 'container',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['follow'] = {
        'name': 'follow',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['previous'] = {
        'name': 'previous',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['since_seconds'] = {
        'name': 'sinceSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['since_time'] = {
        'name': 'sinceTime',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timestamps'] = {
        'name': 'timestamps',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['tail_lines'] = {
        'name': 'tailLines',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['limit_bytes'] = {
        'name': 'limitBytes',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods_name_portforward(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods/{name}/portforward'

    _get_type_ = 'string'

    _get_ = {}
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods_name_proxy(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods/{name}/proxy'

    _get_type_ = 'string'

    _get_ = {}
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _head_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _options_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods_name_proxy_path(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}'

    _get_type_ = 'string'

    _get_ = {}
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _head_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _options_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_pods_name_status(EndPoint):

    path = '/api/v1/namespaces/{namespace}/pods/{name}/status'

    _get_type_ = 'v1.Pod'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Pod'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Pod',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Pod'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_podtemplates(EndPoint):

    path = '/api/v1/namespaces/{namespace}/podtemplates'

    _get_type_ = 'v1.PodTemplateList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.PodTemplate'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.PodTemplate',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_podtemplates_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/podtemplates/{name}'

    _get_type_ = 'v1.PodTemplate'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.PodTemplate'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.PodTemplate',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.PodTemplate'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_replicationcontrollers(EndPoint):

    path = '/api/v1/namespaces/{namespace}/replicationcontrollers'

    _get_type_ = 'v1.ReplicationControllerList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ReplicationController'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ReplicationController',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_replicationcontrollers_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}'

    _get_type_ = 'v1.ReplicationController'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ReplicationController'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ReplicationController',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ReplicationController'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_replicationcontrollers_name_scale(EndPoint):

    path = '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale'

    _get_type_ = 'v1.Scale'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Scale'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Scale',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Scale'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_replicationcontrollers_name_status(EndPoint):

    path = '/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status'

    _get_type_ = 'v1.ReplicationController'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ReplicationController'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ReplicationController',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ReplicationController'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_resourcequotas(EndPoint):

    path = '/api/v1/namespaces/{namespace}/resourcequotas'

    _get_type_ = 'v1.ResourceQuotaList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ResourceQuota'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ResourceQuota',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_resourcequotas_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/resourcequotas/{name}'

    _get_type_ = 'v1.ResourceQuota'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ResourceQuota'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ResourceQuota',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ResourceQuota'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_resourcequotas_name_status(EndPoint):

    path = '/api/v1/namespaces/{namespace}/resourcequotas/{name}/status'

    _get_type_ = 'v1.ResourceQuota'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ResourceQuota'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ResourceQuota',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ResourceQuota'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_secrets(EndPoint):

    path = '/api/v1/namespaces/{namespace}/secrets'

    _get_type_ = 'v1.SecretList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Secret'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Secret',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_secrets_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/secrets/{name}'

    _get_type_ = 'v1.Secret'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Secret'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Secret',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Secret'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_serviceaccounts(EndPoint):

    path = '/api/v1/namespaces/{namespace}/serviceaccounts'

    _get_type_ = 'v1.ServiceAccountList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ServiceAccount'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ServiceAccount',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_serviceaccounts_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/serviceaccounts/{name}'

    _get_type_ = 'v1.ServiceAccount'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ServiceAccount'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ServiceAccount',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ServiceAccount'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_services(EndPoint):

    path = '/api/v1/namespaces/{namespace}/services'

    _get_type_ = 'v1.ServiceList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Service'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Service',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_services_name(EndPoint):

    path = '/api/v1/namespaces/{namespace}/services/{name}'

    _get_type_ = 'v1.Service'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Service'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Service',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Service'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_services_name_proxy(EndPoint):

    path = '/api/v1/namespaces/{namespace}/services/{name}/proxy'

    _get_type_ = 'string'

    _get_ = {}
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _head_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _options_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_services_name_proxy_path(EndPoint):

    path = '/api/v1/namespaces/{namespace}/services/{name}/proxy/{path}'

    _get_type_ = 'string'

    _get_ = {}
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _head_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _options_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_services_name_status(EndPoint):

    path = '/api/v1/namespaces/{namespace}/services/{name}/status'

    _get_type_ = 'v1.Service'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Service'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Service',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Service'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace(EndPoint):

    path = '/api/v1/namespaces/{namespace}'

    _get_type_ = 'v1.Namespace'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Namespace'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Namespace',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Namespace'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_finalize(EndPoint):

    path = '/api/v1/namespaces/{namespace}/finalize'

    _put_type_ = 'v1.Namespace'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Namespace',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_namespaces_namespace_status(EndPoint):

    path = '/api/v1/namespaces/{namespace}/status'

    _get_type_ = 'v1.Namespace'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Namespace'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Namespace',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Namespace'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_nodes(EndPoint):

    path = '/api/v1/nodes'

    _get_type_ = 'v1.NodeList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Node'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Node',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_api_v1_nodes_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_api_v1_nodes_name(EndPoint):

    path = '/api/v1/nodes/{name}'

    _get_type_ = 'v1.Node'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Node'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Node',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Node'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_nodes_name_proxy(EndPoint):

    path = '/api/v1/nodes/{name}/proxy'

    _get_type_ = 'string'

    _get_ = {}
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_nodes_name_proxy_path(EndPoint):

    path = '/api/v1/nodes/{name}/proxy/{path}'

    _get_type_ = 'string'

    _get_ = {}
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_nodes_name_status(EndPoint):

    path = '/api/v1/nodes/{name}/status'

    _get_type_ = 'v1.Node'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Node'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Node',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Node'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_persistentvolumeclaims(EndPoint):

    path = '/api/v1/persistentvolumeclaims'

    _get_type_ = 'v1.PersistentVolumeClaimList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.PersistentVolumeClaim'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.PersistentVolumeClaim',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_persistentvolumes(EndPoint):

    path = '/api/v1/persistentvolumes'

    _get_type_ = 'v1.PersistentVolumeList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.PersistentVolume'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.PersistentVolume',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_api_v1_persistentvolumes_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_api_v1_persistentvolumes_name(EndPoint):

    path = '/api/v1/persistentvolumes/{name}'

    _get_type_ = 'v1.PersistentVolume'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.PersistentVolume'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.PersistentVolume',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.PersistentVolume'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_persistentvolumes_name_status(EndPoint):

    path = '/api/v1/persistentvolumes/{name}/status'

    _get_type_ = 'v1.PersistentVolume'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.PersistentVolume'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.PersistentVolume',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.PersistentVolume'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_pods(EndPoint):

    path = '/api/v1/pods'

    _get_type_ = 'v1.PodList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Pod'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Pod',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_podtemplates(EndPoint):

    path = '/api/v1/podtemplates'

    _get_type_ = 'v1.PodTemplateList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.PodTemplate'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.PodTemplate',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_proxy_namespaces_namespace_pods_name(EndPoint):

    path = '/api/v1/proxy/namespaces/{namespace}/pods/{name}'

    _get_type_ = 'string'

    _get_ = {}
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_proxy_namespaces_namespace_pods_name_path(EndPoint):

    path = '/api/v1/proxy/namespaces/{namespace}/pods/{name}/{path}'

    _get_type_ = 'string'

    _get_ = {}
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_proxy_namespaces_namespace_services_name(EndPoint):

    path = '/api/v1/proxy/namespaces/{namespace}/services/{name}'

    _get_type_ = 'string'

    _get_ = {}
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_proxy_namespaces_namespace_services_name_path(EndPoint):

    path = '/api/v1/proxy/namespaces/{namespace}/services/{name}/{path}'

    _get_type_ = 'string'

    _get_ = {}
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_proxy_nodes_name(EndPoint):

    path = '/api/v1/proxy/nodes/{name}'

    _get_type_ = 'string'

    _get_ = {}
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_proxy_nodes_name_path(EndPoint):

    path = '/api/v1/proxy/nodes/{name}/{path}'

    _get_type_ = 'string'

    _get_ = {}
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'string'

    _put_ = {}
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('put', _path_, _params_, _body_)

    _post_type_ = 'string'

    _post_ = {}
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'string'

    _delete_ = {}
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    _head_type_ = 'string'

    _head_ = {}
    _head_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _head_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def head(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._head_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('head', _path_, _params_, _body_)

    _options_type_ = 'string'

    _options_ = {}
    _options_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _options_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def options(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._options_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('options', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_replicationcontrollers(EndPoint):

    path = '/api/v1/replicationcontrollers'

    _get_type_ = 'v1.ReplicationControllerList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ReplicationController'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ReplicationController',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_resourcequotas(EndPoint):

    path = '/api/v1/resourcequotas'

    _get_type_ = 'v1.ResourceQuotaList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ResourceQuota'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ResourceQuota',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_secrets(EndPoint):

    path = '/api/v1/secrets'

    _get_type_ = 'v1.SecretList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Secret'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Secret',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_securitycontextconstraints(EndPoint):

    path = '/api/v1/securitycontextconstraints'

    _get_type_ = 'v1.SecurityContextConstraintsList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.SecurityContextConstraints'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.SecurityContextConstraints',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_api_v1_securitycontextconstraints_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_api_v1_securitycontextconstraints_name(EndPoint):

    path = '/api/v1/securitycontextconstraints/{name}'

    _get_type_ = 'v1.SecurityContextConstraints'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.SecurityContextConstraints'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.SecurityContextConstraints',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.SecurityContextConstraints'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_serviceaccounts(EndPoint):

    path = '/api/v1/serviceaccounts'

    _get_type_ = 'v1.ServiceAccountList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ServiceAccount'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ServiceAccount',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_api_v1_services(EndPoint):

    path = '/api/v1/services'

    _get_type_ = 'v1.ServiceList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Service'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Service',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1(EndPoint):

    path = '/oapi/v1'

    _get_type_ = 'unversioned.APIResourceList'

    _get_ = {}

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_appliedclusterresourcequotas(EndPoint):

    path = '/oapi/v1/appliedclusterresourcequotas'

    _get_type_ = 'v1.AppliedClusterResourceQuotaList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_buildconfigs(EndPoint):

    path = '/oapi/v1/buildconfigs'

    _get_type_ = 'v1.BuildConfigList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.BuildConfig'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.BuildConfig',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_builds(EndPoint):

    path = '/oapi/v1/builds'

    _get_type_ = 'v1.BuildList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Build'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Build',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_clusternetworks(EndPoint):

    path = '/oapi/v1/clusternetworks'

    _get_type_ = 'v1.ClusterNetworkList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ClusterNetwork'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterNetwork',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_clusternetworks_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_clusternetworks_name(EndPoint):

    path = '/oapi/v1/clusternetworks/{name}'

    _get_type_ = 'v1.ClusterNetwork'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ClusterNetwork'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterNetwork',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ClusterNetwork'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_clusterpolicies(EndPoint):

    path = '/oapi/v1/clusterpolicies'

    _get_type_ = 'v1.ClusterPolicyList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ClusterPolicy'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterPolicy',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_clusterpolicies_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_clusterpolicies_name(EndPoint):

    path = '/oapi/v1/clusterpolicies/{name}'

    _get_type_ = 'v1.ClusterPolicy'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ClusterPolicy'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterPolicy',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ClusterPolicy'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_clusterpolicybindings(EndPoint):

    path = '/oapi/v1/clusterpolicybindings'

    _get_type_ = 'v1.ClusterPolicyBindingList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ClusterPolicyBinding'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterPolicyBinding',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_clusterpolicybindings_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_clusterpolicybindings_name(EndPoint):

    path = '/oapi/v1/clusterpolicybindings/{name}'

    _get_type_ = 'v1.ClusterPolicyBinding'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ClusterPolicyBinding'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterPolicyBinding',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ClusterPolicyBinding'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_clusterresourcequotas(EndPoint):

    path = '/oapi/v1/clusterresourcequotas'

    _get_type_ = 'v1.ClusterResourceQuotaList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ClusterResourceQuota'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterResourceQuota',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_clusterresourcequotas_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_clusterresourcequotas_name(EndPoint):

    path = '/oapi/v1/clusterresourcequotas/{name}'

    _get_type_ = 'v1.ClusterResourceQuota'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ClusterResourceQuota'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterResourceQuota',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ClusterResourceQuota'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_clusterresourcequotas_name_status(EndPoint):

    path = '/oapi/v1/clusterresourcequotas/{name}/status'

    _get_type_ = 'v1.ClusterResourceQuota'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ClusterResourceQuota'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterResourceQuota',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ClusterResourceQuota'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_clusterrolebindings(EndPoint):

    path = '/oapi/v1/clusterrolebindings'

    _get_type_ = 'v1.ClusterRoleBindingList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ClusterRoleBinding'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterRoleBinding',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_clusterrolebindings_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_clusterrolebindings_name(EndPoint):

    path = '/oapi/v1/clusterrolebindings/{name}'

    _get_type_ = 'v1.ClusterRoleBinding'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ClusterRoleBinding'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterRoleBinding',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ClusterRoleBinding'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_clusterroles(EndPoint):

    path = '/oapi/v1/clusterroles'

    _get_type_ = 'v1.ClusterRoleList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ClusterRole'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterRole',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_clusterroles_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_clusterroles_name(EndPoint):

    path = '/oapi/v1/clusterroles/{name}'

    _get_type_ = 'v1.ClusterRole'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ClusterRole'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ClusterRole',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ClusterRole'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_deploymentconfigrollbacks(EndPoint):

    path = '/oapi/v1/deploymentconfigrollbacks'

    _post_type_ = 'v1.DeploymentConfigRollback'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.DeploymentConfigRollback',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_deploymentconfigs(EndPoint):

    path = '/oapi/v1/deploymentconfigs'

    _get_type_ = 'v1.DeploymentConfigList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.DeploymentConfig'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.DeploymentConfig',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_egressnetworkpolicies(EndPoint):

    path = '/oapi/v1/egressnetworkpolicies'

    _get_type_ = 'v1.EgressNetworkPolicyList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.EgressNetworkPolicy'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.EgressNetworkPolicy',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_groups(EndPoint):

    path = '/oapi/v1/groups'

    _get_type_ = 'v1.GroupList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Group'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Group',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_groups_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_groups_name(EndPoint):

    path = '/oapi/v1/groups/{name}'

    _get_type_ = 'v1.Group'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Group'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Group',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Group'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_hostsubnets(EndPoint):

    path = '/oapi/v1/hostsubnets'

    _get_type_ = 'v1.HostSubnetList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.HostSubnet'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.HostSubnet',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_hostsubnets_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_hostsubnets_name(EndPoint):

    path = '/oapi/v1/hostsubnets/{name}'

    _get_type_ = 'v1.HostSubnet'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.HostSubnet'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.HostSubnet',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.HostSubnet'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_identities(EndPoint):

    path = '/oapi/v1/identities'

    _get_type_ = 'v1.IdentityList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Identity'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Identity',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_identities_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_identities_name(EndPoint):

    path = '/oapi/v1/identities/{name}'

    _get_type_ = 'v1.Identity'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Identity'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Identity',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Identity'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_images(EndPoint):

    path = '/oapi/v1/images'

    _get_type_ = 'v1.ImageList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Image'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Image',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_images_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_images_name(EndPoint):

    path = '/oapi/v1/images/{name}'

    _get_type_ = 'v1.Image'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Image'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Image',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Image'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_imagesignatures(EndPoint):

    path = '/oapi/v1/imagesignatures'

    _post_type_ = 'v1.ImageSignature'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ImageSignature',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_imagesignatures_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_imagesignatures_name(EndPoint):

    path = '/oapi/v1/imagesignatures/{name}'

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_imagestreamimports(EndPoint):

    path = '/oapi/v1/imagestreamimports'

    _post_type_ = 'v1.ImageStreamImport'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStreamImport',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_imagestreammappings(EndPoint):

    path = '/oapi/v1/imagestreammappings'

    _post_type_ = 'v1.ImageStreamMapping'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStreamMapping',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_imagestreams(EndPoint):

    path = '/oapi/v1/imagestreams'

    _get_type_ = 'v1.ImageStreamList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ImageStream'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStream',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_imagestreamtags(EndPoint):

    path = '/oapi/v1/imagestreamtags'

    _get_type_ = 'v1.ImageStreamTagList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ImageStreamTag'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStreamTag',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_localresourceaccessreviews(EndPoint):

    path = '/oapi/v1/localresourceaccessreviews'

    _post_type_ = 'v1.LocalResourceAccessReview'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.LocalResourceAccessReview',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_localsubjectaccessreviews(EndPoint):

    path = '/oapi/v1/localsubjectaccessreviews'

    _post_type_ = 'v1.LocalSubjectAccessReview'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.LocalSubjectAccessReview',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_appliedclusterresourcequotas(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/appliedclusterresourcequotas'

    _get_type_ = 'v1.AppliedClusterResourceQuotaList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_appliedclusterresourcequotas_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/appliedclusterresourcequotas/{name}'

    _get_type_ = 'v1.AppliedClusterResourceQuota'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_buildconfigs(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/buildconfigs'

    _get_type_ = 'v1.BuildConfigList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.BuildConfig'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.BuildConfig',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_buildconfigs_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/buildconfigs/{name}'

    _get_type_ = 'v1.BuildConfig'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.BuildConfig'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.BuildConfig',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.BuildConfig'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_buildconfigs_name_instantiate(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/buildconfigs/{name}/instantiate'

    _post_type_ = 'v1.BuildRequest'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.BuildRequest',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_buildconfigs_name_instantiatebinary(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/buildconfigs/{name}/instantiatebinary'

    _post_type_ = 'string'

    _post_ = {}
    _post_['as_file'] = {
        'name': 'asFile',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['revision.commit'] = {
        'name': 'revision.commit',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['revision.message'] = {
        'name': 'revision.message',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['revision.author_name'] = {
        'name': 'revision.authorName',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['revision.author_email'] = {
        'name': 'revision.authorEmail',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['revision.committer_name'] = {
        'name': 'revision.committerName',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['revision.committer_email'] = {
        'name': 'revision.committerEmail',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_buildconfigs_name_webhooks(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks'

    _post_type_ = 'string'

    _post_ = {}
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_buildconfigs_name_webhooks_path(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks/{path}'

    _post_type_ = 'string'

    _post_ = {}
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['path'] = {
        'name': 'path',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_builds(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/builds'

    _get_type_ = 'v1.BuildList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Build'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Build',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_builds_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/builds/{name}'

    _get_type_ = 'v1.Build'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Build'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Build',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Build'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_builds_name_clone(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/builds/{name}/clone'

    _post_type_ = 'v1.BuildRequest'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.BuildRequest',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_builds_name_details(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/builds/{name}/details'

    _put_type_ = 'v1.Build'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Build',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_builds_name_log(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/builds/{name}/log'

    _get_type_ = 'v1.BuildLog'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['container'] = {
        'name': 'container',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['follow'] = {
        'name': 'follow',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['previous'] = {
        'name': 'previous',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['since_seconds'] = {
        'name': 'sinceSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['since_time'] = {
        'name': 'sinceTime',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timestamps'] = {
        'name': 'timestamps',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['tail_lines'] = {
        'name': 'tailLines',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['limit_bytes'] = {
        'name': 'limitBytes',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['nowait'] = {
        'name': 'nowait',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['version'] = {
        'name': 'version',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_deploymentconfigrollbacks(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/deploymentconfigrollbacks'

    _post_type_ = 'v1.DeploymentConfigRollback'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.DeploymentConfigRollback',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_deploymentconfigs(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/deploymentconfigs'

    _get_type_ = 'v1.DeploymentConfigList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.DeploymentConfig'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.DeploymentConfig',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_deploymentconfigs_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}'

    _get_type_ = 'v1.DeploymentConfig'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.DeploymentConfig'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.DeploymentConfig',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.DeploymentConfig'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_deploymentconfigs_name_log(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/log'

    _get_type_ = 'v1.DeploymentLog'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['container'] = {
        'name': 'container',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['follow'] = {
        'name': 'follow',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['previous'] = {
        'name': 'previous',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['since_seconds'] = {
        'name': 'sinceSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['since_time'] = {
        'name': 'sinceTime',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timestamps'] = {
        'name': 'timestamps',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['tail_lines'] = {
        'name': 'tailLines',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['limit_bytes'] = {
        'name': 'limitBytes',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['nowait'] = {
        'name': 'nowait',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['version'] = {
        'name': 'version',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_deploymentconfigs_name_rollback(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/rollback'

    _post_type_ = 'v1.DeploymentConfigRollback'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.DeploymentConfigRollback',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _post_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_deploymentconfigs_name_scale(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/scale'

    _get_type_ = 'v1beta1.Scale'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1beta1.Scale'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1beta1.Scale',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1beta1.Scale'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_deploymentconfigs_name_status(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/deploymentconfigs/{name}/status'

    _put_type_ = 'v1.DeploymentConfig'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.DeploymentConfig',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_egressnetworkpolicies(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/egressnetworkpolicies'

    _get_type_ = 'v1.EgressNetworkPolicyList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.EgressNetworkPolicy'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.EgressNetworkPolicy',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_egressnetworkpolicies_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/egressnetworkpolicies/{name}'

    _get_type_ = 'v1.EgressNetworkPolicy'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.EgressNetworkPolicy'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.EgressNetworkPolicy',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.EgressNetworkPolicy'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_generatedeploymentconfigs_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/generatedeploymentconfigs/{name}'

    _get_type_ = 'v1.DeploymentConfig'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_imagestreamimages_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/imagestreamimages/{name}'

    _get_type_ = 'v1.ImageStreamImage'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_imagestreamimports(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/imagestreamimports'

    _post_type_ = 'v1.ImageStreamImport'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStreamImport',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_imagestreammappings(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/imagestreammappings'

    _post_type_ = 'v1.ImageStreamMapping'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStreamMapping',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_imagestreams(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/imagestreams'

    _get_type_ = 'v1.ImageStreamList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ImageStream'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStream',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_imagestreams_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/imagestreams/{name}'

    _get_type_ = 'v1.ImageStream'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ImageStream'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStream',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ImageStream'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_imagestreams_name_secrets(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/imagestreams/{name}/secrets'

    _get_type_ = 'v1.SecretList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_imagestreams_name_status(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/imagestreams/{name}/status'

    _put_type_ = 'v1.ImageStream'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStream',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_imagestreamtags(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/imagestreamtags'

    _get_type_ = 'v1.ImageStreamTagList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ImageStreamTag'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStreamTag',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_imagestreamtags_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/imagestreamtags/{name}'

    _get_type_ = 'v1.ImageStreamTag'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.ImageStreamTag'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.ImageStreamTag',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.ImageStreamTag'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_localresourceaccessreviews(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/localresourceaccessreviews'

    _post_type_ = 'v1.LocalResourceAccessReview'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.LocalResourceAccessReview',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_localsubjectaccessreviews(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/localsubjectaccessreviews'

    _post_type_ = 'v1.LocalSubjectAccessReview'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.LocalSubjectAccessReview',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_policies(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/policies'

    _get_type_ = 'v1.PolicyList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Policy'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Policy',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_policies_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/policies/{name}'

    _get_type_ = 'v1.Policy'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Policy'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Policy',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Policy'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_policybindings(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/policybindings'

    _get_type_ = 'v1.PolicyBindingList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.PolicyBinding'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.PolicyBinding',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_policybindings_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/policybindings/{name}'

    _get_type_ = 'v1.PolicyBinding'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.PolicyBinding'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.PolicyBinding',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.PolicyBinding'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_processedtemplates(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/processedtemplates'

    _post_type_ = 'v1.Template'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Template',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_resourceaccessreviews(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/resourceaccessreviews'

    _post_type_ = 'v1.ResourceAccessReview'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ResourceAccessReview',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_rolebindings(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/rolebindings'

    _get_type_ = 'v1.RoleBindingList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.RoleBinding'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.RoleBinding',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_rolebindings_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/rolebindings/{name}'

    _get_type_ = 'v1.RoleBinding'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.RoleBinding'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.RoleBinding',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.RoleBinding'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_roles(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/roles'

    _get_type_ = 'v1.RoleList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Role'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Role',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_roles_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/roles/{name}'

    _get_type_ = 'v1.Role'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Role'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Role',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Role'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_routes(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/routes'

    _get_type_ = 'v1.RouteList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Route'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Route',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_routes_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/routes/{name}'

    _get_type_ = 'v1.Route'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Route'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Route',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Route'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_routes_name_status(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/routes/{name}/status'

    _put_type_ = 'v1.Route'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Route',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_selfsubjectrulesreviews(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/selfsubjectrulesreviews'

    _post_type_ = 'v1.SelfSubjectRulesReview'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.SelfSubjectRulesReview',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_subjectaccessreviews(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/subjectaccessreviews'

    _post_type_ = 'v1.SubjectAccessReview'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.SubjectAccessReview',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_templates(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/templates'

    _get_type_ = 'v1.TemplateList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Template'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Template',
        'param_type': 'body',
        'required': True,
    }
    _post_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_namespaces_namespace_templates_name(EndPoint):

    path = '/oapi/v1/namespaces/{namespace}/templates/{name}'

    _get_type_ = 'v1.Template'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Template'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Template',
        'param_type': 'body',
        'required': True,
    }
    _put_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Template'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['namespace'] = {
        'name': 'namespace',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_netnamespaces(EndPoint):

    path = '/oapi/v1/netnamespaces'

    _get_type_ = 'v1.NetNamespaceList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.NetNamespace'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.NetNamespace',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_netnamespaces_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_netnamespaces_name(EndPoint):

    path = '/oapi/v1/netnamespaces/{name}'

    _get_type_ = 'v1.NetNamespace'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.NetNamespace'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.NetNamespace',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.NetNamespace'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_oauthaccesstokens(EndPoint):

    path = '/oapi/v1/oauthaccesstokens'

    _get_type_ = 'v1.OAuthAccessTokenList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.OAuthAccessToken'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.OAuthAccessToken',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_oauthaccesstokens_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_oauthaccesstokens_name(EndPoint):

    path = '/oapi/v1/oauthaccesstokens/{name}'

    _get_type_ = 'v1.OAuthAccessToken'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.OAuthAccessToken'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.OAuthAccessToken',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.OAuthAccessToken'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_oauthauthorizetokens(EndPoint):

    path = '/oapi/v1/oauthauthorizetokens'

    _get_type_ = 'v1.OAuthAuthorizeTokenList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.OAuthAuthorizeToken'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.OAuthAuthorizeToken',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_oauthauthorizetokens_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_oauthauthorizetokens_name(EndPoint):

    path = '/oapi/v1/oauthauthorizetokens/{name}'

    _get_type_ = 'v1.OAuthAuthorizeToken'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.OAuthAuthorizeToken'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.OAuthAuthorizeToken',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.OAuthAuthorizeToken'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_oauthclientauthorizations(EndPoint):

    path = '/oapi/v1/oauthclientauthorizations'

    _get_type_ = 'v1.OAuthClientAuthorizationList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.OAuthClientAuthorization'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.OAuthClientAuthorization',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_oauthclientauthorizations_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_oauthclientauthorizations_name(EndPoint):

    path = '/oapi/v1/oauthclientauthorizations/{name}'

    _get_type_ = 'v1.OAuthClientAuthorization'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.OAuthClientAuthorization'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.OAuthClientAuthorization',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.OAuthClientAuthorization'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_oauthclients(EndPoint):

    path = '/oapi/v1/oauthclients'

    _get_type_ = 'v1.OAuthClientList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.OAuthClient'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.OAuthClient',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_oauthclients_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_oauthclients_name(EndPoint):

    path = '/oapi/v1/oauthclients/{name}'

    _get_type_ = 'v1.OAuthClient'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.OAuthClient'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.OAuthClient',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.OAuthClient'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_policies(EndPoint):

    path = '/oapi/v1/policies'

    _get_type_ = 'v1.PolicyList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Policy'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Policy',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_policybindings(EndPoint):

    path = '/oapi/v1/policybindings'

    _get_type_ = 'v1.PolicyBindingList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.PolicyBinding'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.PolicyBinding',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_processedtemplates(EndPoint):

    path = '/oapi/v1/processedtemplates'

    _post_type_ = 'v1.Template'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Template',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_projectrequests(EndPoint):

    path = '/oapi/v1/projectrequests'

    _get_type_ = 'unversioned.Status'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.ProjectRequest'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ProjectRequest',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_projects(EndPoint):

    path = '/oapi/v1/projects'

    _get_type_ = 'v1.ProjectList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Project'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Project',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_projects_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_projects_name(EndPoint):

    path = '/oapi/v1/projects/{name}'

    _get_type_ = 'v1.Project'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.Project'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.Project',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.Project'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_resourceaccessreviews(EndPoint):

    path = '/oapi/v1/resourceaccessreviews'

    _post_type_ = 'v1.ResourceAccessReview'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.ResourceAccessReview',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_rolebindings(EndPoint):

    path = '/oapi/v1/rolebindings'

    _get_type_ = 'v1.RoleBindingList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.RoleBinding'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.RoleBinding',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_roles(EndPoint):

    path = '/oapi/v1/roles'

    _get_type_ = 'v1.RoleList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Role'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Role',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_routes(EndPoint):

    path = '/oapi/v1/routes'

    _get_type_ = 'v1.RouteList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Route'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Route',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_selfsubjectrulesreviews(EndPoint):

    path = '/oapi/v1/selfsubjectrulesreviews'

    _post_type_ = 'v1.SelfSubjectRulesReview'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.SelfSubjectRulesReview',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_subjectaccessreviews(EndPoint):

    path = '/oapi/v1/subjectaccessreviews'

    _post_type_ = 'v1.SubjectAccessReview'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.SubjectAccessReview',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_templates(EndPoint):

    path = '/oapi/v1/templates'

    _get_type_ = 'v1.TemplateList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.Template'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.Template',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_useridentitymappings(EndPoint):

    path = '/oapi/v1/useridentitymappings'

    _post_type_ = 'v1.UserIdentityMapping'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.UserIdentityMapping',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_useridentitymappings_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_useridentitymappings_name(EndPoint):

    path = '/oapi/v1/useridentitymappings/{name}'

    _get_type_ = 'v1.UserIdentityMapping'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.UserIdentityMapping'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.UserIdentityMapping',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.UserIdentityMapping'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

@register_endpoint
class EndPoint_oapi_v1_users(EndPoint):

    path = '/oapi/v1/users'

    _get_type_ = 'v1.UserList'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _post_type_ = 'v1.User'

    _post_ = {}
    _post_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _post_['body'] = {
        'name': 'body',
        'type': 'v1.User',
        'param_type': 'body',
        'required': True,
    }

    def post(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._post_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('post', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['label_selector'] = {
        'name': 'labelSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['field_selector'] = {
        'name': 'fieldSelector',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['watch'] = {
        'name': 'watch',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _delete_['resource_version'] = {
        'name': 'resourceVersion',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['timeout_seconds'] = {
        'name': 'timeoutSeconds',
        'type': 'integer',
        'param_type': 'query',
        'required': False,
    }

    def delete(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('delete', _path_, _params_, _body_)

    def __call__(self, *, name):
        params = dict(self.params)
        params['name'] = name
        return EndPoint_oapi_v1_users_name(self.client, None, self._async_, **params)

@register_endpoint
class EndPoint_oapi_v1_users_name(EndPoint):

    path = '/oapi/v1/users/{name}'

    _get_type_ = 'v1.User'

    _get_ = {}
    _get_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _get_['export'] = {
        'name': 'export',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['exact'] = {
        'name': 'exact',
        'type': 'boolean',
        'param_type': 'query',
        'required': False,
    }
    _get_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def get(self, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._get_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = None
        return self._request_('get', _path_, _params_, _body_)

    _put_type_ = 'v1.User'

    _put_ = {}
    _put_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _put_['body'] = {
        'name': 'body',
        'type': 'v1.User',
        'param_type': 'body',
        'required': True,
    }
    _put_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def put(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._put_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('put', _path_, _params_, _body_)

    _patch_type_ = 'v1.User'

    _patch_ = {}
    _patch_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _patch_['body'] = {
        'name': 'body',
        'type': 'unversioned.Patch',
        'param_type': 'body',
        'required': True,
    }
    _patch_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def patch(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._patch_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('patch', _path_, _params_, _body_)

    _delete_type_ = 'unversioned.Status'

    _delete_ = {}
    _delete_['pretty'] = {
        'name': 'pretty',
        'type': 'string',
        'param_type': 'query',
        'required': False,
    }
    _delete_['body'] = {
        'name': 'body',
        'type': 'v1.DeleteOptions',
        'param_type': 'body',
        'required': True,
    }
    _delete_['name'] = {
        'name': 'name',
        'type': 'string',
        'param_type': 'path',
        'required': True,
    }

    def delete(self, *, body, **_kwargs_):
        _params_ = dict(self.params)
        _path_ = self.path.format(**_params_)
        for _name_, _param_ in self._delete_.items():
            if _name_ in _kwargs_:
                _params_[_param_['name']] = _kwargs_[_name_]
        _body_ = body
        return self._request_('delete', _path_, _params_, _body_)
