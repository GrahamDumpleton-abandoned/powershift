import powershift.resources as resources

dc = resources.load()

dc.spec.replicas = 3

resources.dump(dc, indent=4, sort_keys=True)
