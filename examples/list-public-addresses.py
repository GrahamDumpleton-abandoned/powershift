import powershift.endpoints as endpoints
import powershift.resources as resources

client = endpoints.Client()

projects = client.oapi.v1.projects.get()

#print(projects)
#print(resources.dumps(projects, indent=4, sort_keys=True))
#print()

def public_address(route):
    host = route.spec.host
    path = route.spec.path or '/'
    if route.spec.tls:
        return 'https://%s%s' % (host, path)
    return 'https://%s%s' % (host, path)

for project in projects.items:
    namespace = project.metadata.name

    print('namespace=%r' % namespace)

    routes = client.oapi.v1.namespaces(namespace=namespace).routes.get()

    for route in routes.items:
        print('    route=%r' % public_address(route))

#print()
#print(resources.dumps(routes, indent=4, sort_keys=True))
