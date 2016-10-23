import os

from jinja2 import Environment, PackageLoader

__here__ = os.path.dirname(__file__)

env = Environment(loader=PackageLoader('powershift', 'templates'), trim_blocks=True, lstrip_blocks=True)

def get_template(name, parent=None, globals=None):
    return env.get_template(name, parent, globals)

def list_templates(extensions=None, filter_func=None):
    return env.list_templates(extensions, filter_func)
