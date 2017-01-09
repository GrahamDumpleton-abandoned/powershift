import sys
import asyncio

import powershift.endpoints as endpoints

async def run_query():
    namespace = sys.argv[1]

    print('namespace=%r' % namespace)

    client = endpoints.AsyncClient()

    pods = await client.api.v1.namespaces(namespace=namespace).pods.get()

    for pod in pods.items:
        print('    OBJECT %s pod=%r' % (pod.metadata.resource_version, pod.metadata.name))

    resource_version = pods.metadata.resource_version

    while True:
        try:
            async with client.api.v1.namespaces(namespace=namespace).pods.get(watch='', resource_version=resource_version, timeout_seconds=10) as items:
                async for item in items:
                    action = item['type']
                    pod = item['object']

                    print('    %s %s pod=%r' % (action, pod.metadata.resource_version, pod.metadata.name))

                    resource_version = pod.metadata.resource_version
        except Exception:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(run_query())
