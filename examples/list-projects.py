import powershift.endpoints as endpoints
import powershift.resources as resources

client = endpoints.Client()

projects = client.oapi.v1.projects.get()

#print(resources.dumps(projects, indent=4, sort_keys=True))
#print()

for project in projects.items:
    print('namespace=%r' % project.metadata.name)
    print('    description=%r' % project.metadata.annotations['openshift.io/description'])
    print('    display-name=%r' % project.metadata.annotations['openshift.io/display-name'])
    print()
