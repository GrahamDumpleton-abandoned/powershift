from openshift3.resources import load, dump, v1_EnvVar

resource = load()

variables = resource.spec.template.spec.containers[0].env

variables.append(v1_EnvVar(name='VAR1', value='VALUE'))
variables.append(v1_EnvVar(name='VAR2', value='VALUE'))

dump(resource, indent=4, sort_keys=True)
