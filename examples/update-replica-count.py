from openshift3.resources import load, dump

resource = load()

resource.spec.replicas = 3

dump(resource, indent=4, sort_keys=True)
