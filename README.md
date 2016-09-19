# Python library for working with OpenShift 3

This package provides a Python library for working with OpenShift 3.

The library will provide the capability to work with OpenShift/Kubernetes resource objects, as well as endpoints for communicating with the OpenShift REST API.

The package requires Python 3 and will not work with Python 2.

## Manipulating resource objects

The library always starts and ends with JSON definitions of the OpenShift/Kubernetes resource objects. The functions for loading the JSON definitions to create in memory representations of the resources are:

* ``openshift3.resources.load(path=None)`` - Loads resources from JSON from a file with the specified ``path``, or from standard input if no ``path`` specified.
* ``openshift3.resources.loads(data)`` - Loads resources from JSON specified as string data.

The functions for dumping JSON definitions from the in memory representations of the resources are:

* ``openshift3.resources.dump(obj, path=None, indent=None, sort_keys=False)`` - Saves resources as JSON to the specified ``path``, or to ``stdout`` if no ``path`` supplied. The JSON can be formatted in a more readable form by supplying an ``indent`` and electing to ``sort_keys``.
* ``openshift3.resources.dumps(obj, indent=None, sort_keys=False)`` - Returns resources as JSON string data. The JSON can be formatted in a more readable form by supplying an ``indent`` and electing to ``sort_keys``.

Example code which takes a ``DeploymentConfig`` from ``stdin``, updating the replica count and outputting the result to ``stdout`` is:

```
import openshift3.resources as resources

dc = resources.load()

dc.spec.replicas = 3

resources.dump(dc, indent=4, sort_keys=True)
```

Example code which takes a ``DeploymentConfig`` from ``stdin``, adding some environment variables and outputting the result to ``stdout`` is:

```
import openshift3.resources as resources

dc = resources.load()

env = dc.spec.template.spec.containers[0].env

env.append(resources.v1_EnvVar(name='VAR1', value='VALUE'))
env.append(resources.v1_EnvVar(name='VAR2', value='VALUE'))

resources.dump(dc, indent=4, sort_keys=True)
```

Scripts using the library could be used to make multiple changes to resource objects for a deployed application on the fly by using a command of the form:

```
oc get dc myapp -o json | python script.py | oc replace -f -
```

Note that all attribute and parameter names used snake case and not camel case.

## Calling the OpenShift REST API

Requests can be made against the OpenShift REST API by first creating a client object:

* ``openshift3.endpoints.Client(host=None, token=None, verify=None)`` - Create a client object for ``host`` by passing ``'hostname'``, optionally including a port by specifying ``'hostname:port'``. The API access ``token`` can be supplied, as can a flag indicating whether certificate verification should be performed for the secure connection. Certificate verification is performed by default.

If the parameters are not being supplied explicitly, they can instead ben supplied using environment variables.

* ``OPENSHIFT_API_HOST`` - The ``hostname`` or ``hostname:port``.
* ``OPENSHIFT_API_TOKEN`` - The API access token.
* ``OPENSHIFT_API_VERIFY`` - Flag indicating whether certificate verification should be performed. Set to ``false`` to disable.

If neither the parameters or environment variables are supplied, it will be assumed it is being run from inside of a container running under OpenShift. The ``host`` will default to ``openshift.default.svc.cluster.local`` and the ``token`` will be read from the file ``/var/run/secrets/kubernetes.io/serviceaccount/token`` if it exists. Certificate verification will be turned off by default in this case.

An example script which prints out the list of pods running in each project is:

```
import openshift3.endpoints as endpoints

client = endpoints.Client()

projects = client.oapi.v1.projects.get()

for project in projects.items:
    namespace = project.metadata.name

    print('namespace=%r' % namespace)

    pods = client.api.v1.namespaces(namespace=namespace).pods.get()

    for pod in pods.items:
        print('pod=%r' % pod.metadata.name)
```

The calling conventions can be derived from the REST API documentation available at:

* [Kubernetes v1 REST API](https://docs.openshift.com/enterprise/latest/rest_api/kubernetes_v1.html).
* [OpenShift Enterprise v1 REST API](https://docs.openshift.com/enterprise/latest/rest_api/openshift_v1.html).

Specifically, by matching to the URL path for an endpoint.

Note that all attribute and parameter names used snake case and not camel case.

The object returned is the in memory representation of resources. These are created automatically from the JSON definitions of the OpenShift/Kubernetes resource objects.

Do note though that the Kubernetes/OpenShift API definitions are inconsistent at some points and have errors. The client library overrides certain aspects of the API definition to fix up problems in the published API. For example, when referring to a namespace, you must always use ``namespace``. The published API mixes ``name`` and ``namespace`` which can cause problems for an automatically generated API such that the package implements.