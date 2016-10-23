import powershift.endpoints as endpoints
import powershift.resources as resources

client = endpoints.Client()

projects = client.oapi.v1.projects.get()

#print(projects)
#print(resources.dumps(projects, indent=4, sort_keys=True))
#print()

for project in projects.items:
    namespace = project.metadata.name

    print('namespace=%r' % namespace)

    pods = client.api.v1.namespaces(namespace=namespace).pods.get()

    for pod in pods.items:
        print('    pod=%r' % pod.metadata.name)

#print()
#print(resources.dumps(pods, indent=4, sort_keys=True))
