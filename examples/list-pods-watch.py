import asyncio

import powershift.endpoints as endpoints
import powershift.resources as resources

client = endpoints.AsyncClient()

async def run_query():
    projects = await client.oapi.v1.projects.get()

    #print(projects)
    #print(resources.dumps(projects, indent=4, sort_keys=True))
    #print()

    project = projects.items[0]
    namespace = project.metadata.name

    print('namespace=%r' % namespace)

    async with client.api.v1.namespaces(namespace=namespace).pods.get(watch='') as items:
        async for item in items:
            action = item['type']
            pod = item['object']
            print('    %s pod=%r' % (action, pod.metadata.name))

loop = asyncio.get_event_loop()

loop.run_until_complete(run_query())
