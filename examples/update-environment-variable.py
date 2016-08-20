import openshift3.resources as resources

dc = resources.load()

env = dc.spec.template.spec.containers[0].env

env.append(resources.v1_EnvVar(name='VAR1', value='VALUE'))
env.append(resources.v1_EnvVar(name='VAR2', value='VALUE'))

resources.dump(dc, indent=4, sort_keys=True)
