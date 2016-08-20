# Python library for working with OpenShift 3

This package provides a Python library for working with OpenShift 3.

The library will provide the capability to work with OpenShift/Kubernetes resource objects, as well as endpoints for communicating with the OpenShift REST API.

At this time only support for manipulating resource objects is implemented.

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
