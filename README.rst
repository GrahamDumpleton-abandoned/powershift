This package provides a Python library for working with the open source
OpenShift Origin project and downstream OpenShift products from Red Hat.

The library will provide the capability to work with OpenShift/Kubernetes
resource objects, as well as endpoints for communicating with the OpenShift
REST API.

A command line client with the name ``powershift`` is also included which
provides additional functionality useful to users of the OpenShift
platform. Base functionality is minimal, but can be extended by installing
additional plugins.

The package requires Python 3.5 and will not work with earlier versions of
Python.

If you are on MacOS X and are using OpenShift Origin 1.4 or later, or
OpenShift Container Platform 3.4 or later, you will need to ensure you are
using Python 3.6 from the Python Software Foundation (PSF), or use Python
3.5 or later, installed using HomeBrew. It is not possible to use Python
3.5 from the PSF, or any other Python installation, which has been compiled
against the OpenSSL version which ships with MacOS X as that only supports
up to TLS 1.1 and newer versions of OpenShift require at least TLS 1.2.

Manipulating resource objects
-----------------------------

The library always starts and ends with JSON definitions of the
OpenShift/Kubernetes resource objects. The functions for loading the JSON
definitions to create in memory representations of the resources are:

* ``powershift.resources.load(path=None)`` - Loads resources from JSON from
  a file with the specified ``path``, or from standard input if no ``path``
  specified.

* ``powershift.resources.loads(data)`` - Loads resources from JSON
  specified as string data.

The functions for dumping JSON definitions from the in memory
representations of the resources are:

* ``powershift.resources.dump(obj, path=None, indent=None, sort_keys=False)`` -
  Saves resources as JSON to the specified ``path``, or to ``stdout`` if no
  ``path`` supplied. The JSON can be formatted in a more readable form by
  supplying an ``indent`` and electing to ``sort_keys``.

* ``powershift.resources.dumps(obj, indent=None, sort_keys=False)`` -
  Returns resources as JSON string data. The JSON can be formatted in a
  more readable form by supplying an ``indent`` and electing to
  ``sort_keys``.

Example code which takes a ``DeploymentConfig`` from ``stdin``, updating
the replica count and outputting the result to ``stdout`` is::

    import powershift.resources as resources

    dc = resources.load()

    dc.spec.replicas = 3

    resources.dump(dc, indent=4, sort_keys=True)

Example code which takes a ``DeploymentConfig`` from ``stdin``, adding some
environment variables and outputting the result to ``stdout`` is::

    import powershift.resources as resources

    dc = resources.load()

    env = dc.spec.template.spec.containers[0].env

    env.append(resources.v1_EnvVar(name='VAR1', value='VALUE'))
    env.append(resources.v1_EnvVar(name='VAR2', value='VALUE'))

    resources.dump(dc, indent=4, sort_keys=True)

Scripts using the library could be used to make multiple changes to
resource objects for a deployed application on the fly by using a command
of the form::

    oc get dc myapp -o json | python script.py | oc replace -f -

Note that all attribute and parameter names use snake case and not camel case.

Calling the OpenShift REST API
------------------------------

Requests can be made against the OpenShift REST API by first creating a
client object:

* ``powershift.endpoints.Client(server=None, token=None, *, user=None, verify=None)`` -
  Create a client object for ``server`` by passing ``'hostname'``,
  optionally including a port by specifying ``'hostname:port'``, or a URL.
  When ``hostname`` is used, it is presumed that a secure connection should
  be used. If using ``oc proxy`` is being used, you will need to supply a
  URL and specify the protocol as ``http`` rather than ``https``. The API
  access ``token`` can be supplied, as can a flag indicating whether
  certificate verification should be performed for a secure connection.
  Certificate verification is performed by default but can be disabled
  using the keyword argument ``verify``. In order to issue the request and
  impersonate a specific user you have rights to impersonate, you can pass
  the keyword argument ``user``.

If the parameters are not being supplied explicitly, they can instead be
supplied using environment variables.

* ``OPENSHIFT_API_SERVER`` - The ``hostname``, ``hostname:port`` or URL.

* ``OPENSHIFT_API_TOKEN`` - The API access token.

* ``OPENSHIFT_API_VERIFY`` - Flag indicating whether certificate
  verification should be performed. Set to ``false`` to disable.

If neither the parameters or environment variables are supplied, it will be
assumed it is being run from inside of a container running under OpenShift.
The ``host`` will default to ``openshift.default.svc.cluster.local`` and
the ``token`` will be read from the file
``/var/run/secrets/kubernetes.io/serviceaccount/token`` if it exists.
Certificate verification will be turned off by default in this case.

An example script which prints out the list of pods running in each project
is::

    import powershift.endpoints as endpoints

    client = endpoints.Client()

    projects = client.oapi.v1.projects.get()

    for project in projects.items:
        namespace = project.metadata.name

        print('namespace=%r' % namespace)

        pods = client.api.v1.namespaces(namespace=namespace).pods.get()

        for pod in pods.items:
            print('pod=%r' % pod.metadata.name)

The client calls in this example are blocking. If you want to use the
client in this manner in an asynchronous system, you will need to execute
the calls in a thread and not within a main event loop callback.

The alternative if implementing any asynchronous system on top of the
``asyncio`` library and Python async/await primitives, is to use the async
variant of the client::

    import asyncio

    import powershift.endpoints as endpoints

    client = endpoints.AsyncClient()

    async def run_query():
        projects = await client.oapi.v1.projects.get()

        for project in projects.items:
            namespace = project.metadata.name

            print('namespace=%r' % namespace)

            pods = await client.api.v1.namespaces(namespace=namespace).pods.get()

            for pod in pods.items:
                print('    pod=%r' % pod.metadata.name)

    loop = asyncio.get_event_loop()

    loop.run_until_complete(run_query())

The calling conventions can be derived from the REST API documentation
available at:

* `Kubernetes v1 REST API`_
* `OpenShift Enterprise v1 REST API`_

.. _`Kubernetes v1 REST API`: https://docs.openshift.com/enterprise/latest/rest_api/kubernetes_v1.html
.. _`OpenShift Enterprise v1 REST API`: https://docs.openshift.com/enterprise/latest/rest_api/openshift_v1.html

Specifically, by matching to the URL path for an endpoint.

Note that all attribute and parameter names use snake case and not camel
case.

The object returned is the in memory representation of resources. These are
created automatically from the JSON definitions of the OpenShift/Kubernetes
resource objects.

Do note though that the Kubernetes/OpenShift API definitions are
inconsistent at some points and have errors. The client library overrides
certain aspects of the API definition to fix up problems in the published
API. For example, when referring to a namespace, you must always use
``namespace``. The published API mixes ``name`` and ``namespace`` which can
cause problems for an automatically generated API such that this package
implements.

Extended command line client
----------------------------

The command line client provided with the package also goes by the name
``powershift``. Executing the command with no arguments will provide a
list of the base commands available.

::

    $ powershift
    Usage: powershift [OPTIONS] COMMAND [ARGS]...

      PowerShift client for OpenShift.

      This client provides additional functionality useful to users of the
      OpenShift platform. Base functionality is minimal, but can be extended by
      installing additional plugins.

      For more details see:

          https://github.com/getwarped/powershift

    Options:
      --help  Show this message and exit.

    Commands:
      completion  Output completion script for specified shell.
      console     Open a browser on the OpenShift web console.
      server      Displays the URL for the OpenShift cluster.

The client uses a plugin structure so that additional commands can be added
for specific purposes by installing additional Python packages which define
the commands.

To enable ``bash`` completion, run ``powershift completion bash --help``
and follow the instructions.
