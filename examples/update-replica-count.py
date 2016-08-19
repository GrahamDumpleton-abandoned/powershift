from openshift3.resources import load, dump

dc = load()

dc.spec.replicas = 3

dump(dc, indent=4, sort_keys=True)
