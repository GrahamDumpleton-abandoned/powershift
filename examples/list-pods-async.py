import asyncio

import powershift.endpoints as endpoints
import powershift.resources as resources

client = endpoints.AsyncClient()

async def run_query():
    projects = await client.oapi.v1.projects.get()

    #print(projects)
    #print(resources.dumps(projects, indent=4, sort_keys=True))
    #print()

    for project in projects.items:
        namespace = project.metadata.name

        print('namespace=%r' % namespace)

        pods = await client.api.v1.namespaces(namespace=namespace).pods.get()

        for pod in pods.items:
            names.append(pod.metadata.name)
            print('    pod=%r' % pod.metadata.name)

            # We are given the pod definition already, but this is just to
            # show how you can also query by the name of the pod.

            pod = await client.api.v1.namespaces(namespace=namespace).pods(name=pod.metadata.name).get() 

            print('        resource_version=%r' % pod.metadata.resource_version)

    #print()
    #print(resources.dumps(pods, indent=4, sort_keys=True))

loop = asyncio.get_event_loop()

loop.run_until_complete(run_query())
