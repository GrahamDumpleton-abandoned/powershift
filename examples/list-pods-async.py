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
            print('    pod=%r' % pod.metadata.name)

    #print()
    #print(resources.dumps(pods, indent=4, sort_keys=True))

loop = asyncio.get_event_loop()

loop.run_until_complete(run_query())
