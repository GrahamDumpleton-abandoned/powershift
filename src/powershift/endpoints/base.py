import os
import requests
import aiohttp
import asyncio

from .. import resources

_bool_tokens = ('1', 'true', 'enabled', 'on')

_internal_token = '/var/run/secrets/kubernetes.io/serviceaccount/token'

class Client(object):

    ASYNC = False

    def __init__(self, server=None, token=None, *, user=None, verify=None):
        self.server = server
        self.token = token
        self.user = user
        self.verify = verify

        if self.server is None:
            self.server = os.environ.get('OPENSHIFT_API_SERVER')

        # For backwards compatibility as changed name.

        if self.server is None:
            self.server = os.environ.get('OPENSHIFT_API_HOST')

        if self.server is None:
            self.server = 'openshift.default.svc.cluster.local'
            if self.token is None and os.path.exists(_internal_token):
                with open(_internal_token) as fp:
                    self.token = fp.read()
                self.verify = False

        if self.token is None:
            self.token = os.environ.get('OPENSHIFT_API_TOKEN', 'unset')

        if self.verify is None:
            self.verify = (os.environ.get('OPENSHIFT_API_VERIFY', 'true').lower()
                    in _bool_tokens)

    @property
    def api(self):
        return EndPoint(self, '/api', self.ASYNC)

    @property
    def oapi(self):
        return EndPoint(self, '/oapi', self.ASYNC)

class AsyncClient(Client):
    ASYNC = True

_endpoint_api_types = {}

def registered_endpoint_types():
    return _endpoint_api_types

def register_endpoint(cls):
    _endpoint_api_types[cls.path] = cls
    return cls

class EndPoint(object):

    path = None

    _delete_ = {}
    _get_ = {}
    _head_ = {}
    _options_ = {}
    _patch_ = {}
    _post_ = {}
    _put_ = {}

    def __init__(self, _client_, _path_=None, _async_=False, **params):
        self.client = _client_

        if _path_:
            self.path = _path_

        self._async_ = _async_

        self.params = params

    def __getattr__(self, name):
        path = '%s/%s' % (self.path, name)
        if path not in _endpoint_api_types:
            if path not in _endpoint_api_types:
                raise AttributeError('invalid API endpoint %r' % path)
            return _endpoint_api_types[fallbackpath](self.client, None,
                    self._async_, **self.params)
        return _endpoint_api_types[path](self.client, None,
                self._async_, **self.params)

    async def _async_request_(self, method, url, params, headers, data):
        connector = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            if data is not None:
                async with getattr(session, method)(url, params=params,
                        headers=headers, data=data) as response:
                    data = await response.read()
                    result = resources.loads(data.decode('UTF-8'))
            else:
                async with getattr(session, method)(url, params=params,
                        headers=headers) as response:
                    data = await response.read()
                    result = resources.loads(data.decode('UTF-8'))
        if result.__kind__ != getattr(self, '_%s_type_' % method):
            raise Exception(str(result))
        return result

    def _sync_request_(self, method, url, params, headers, data):
        if data is not None:
            response = getattr(requests, method)(url, headers=headers,
                    params=params, verify=self.client.verify, data=data)
        else:
            response = getattr(requests, method)(url, headers=headers,
                    params=params, verify=self.client.verify)
        result = resources.loads(response.text)
        if result.__kind__ != getattr(self, '_%s_type_' % method):
            raise Exception(str(result))
        return result

    def _request_(self, method, path, params, body):
        server = self.client.server.lower()
        if server.startswith('http://') or server.startswith('https://'):
            url = '%s%s' % (self.client.server, path)
        else:
            url = 'https://%s%s' % (self.client.server, path)
        headers = {}
        headers['Authorization'] = 'Bearer %s' % self.client.token
        if self.client.user is not None:
            headers['Impersonate-User'] = self.client.user
        if body is not None:
            body = resources.dumps(body)
        if self._async_:
            return self._async_request_(method, url, params, headers, body)
        else:
            return self._sync_request_(method, url, params, headers, body)

@register_endpoint
class EndPoint_oapi_v1_namespaces(EndPoint):

    path = '/oapi/v1/namespaces'

    def __call__(self, *, namespace):
        child = self.path + '/{namespace}'
        params = dict(self.params)
        params['namespace'] = namespace
        return EndPoint(self.client, child, self._async_, **params)

# @register_endpoint
# class EndPoint_api_v1_watch(EndPoint):
# 
#     path = '/api/v1/watch'
# 
# @register_endpoint
# class EndPoint_oapi_v1_watch(EndPoint):
# 
#     path = '/oapi/v1/watch'
# 
# @register_endpoint
# class EndPoint_oapi_v1_watch_namespaces(EndPoint):
# 
#     path = '/oapi/v1/watch/namespaces'
# 
#     def __call__(self, *, namespace):
#         child = self.path + '/{namespace}'
#         params = dict(self.params)
#         params['namespace'] = namespace
#         return EndPoint(self.client, child, self._async_, **params)
