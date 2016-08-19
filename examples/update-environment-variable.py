from openshift3.resources import load, dump, v1_EnvVar

dc = load()

env = dc.spec.template.spec.containers[0].env

env.append(v1_EnvVar(name='VAR1', value='VALUE'))
env.append(v1_EnvVar(name='VAR2', value='VALUE'))

dump(dc, indent=4, sort_keys=True)
