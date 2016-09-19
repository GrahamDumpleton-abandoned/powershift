import sys
import os

from setuptools import setup
from distutils.sysconfig import get_python_lib

def _template_files():
    result = []
    prefix = 'src/openshift3/templates'
    for root, dirs, files in os.walk(prefix, topdown=False):
        for name in files:
            if name.endswith('.json'):
                if root == prefix:
                    result.append(os.path.join(root[len(prefix):], name))
                else:
                    result.append(os.path.join(root[len(prefix)+1:], name))
    return result

setup_kwargs = dict(
    name = 'openshift3',
    version = '0.1.0',
    description = 'Python library for working with OpenShift 3.',
    author = 'Graham Dumpleton',
    author_email = 'Graham.Dumpleton@gmail.com',
    license = 'BSD',
    packages = ['openshift3', 'openshift3.resources', 'openshift3.endpoints',
                'openshift3.composer', 'openshift3.templates'],
    package_dir = {'openshift3': 'src/openshift3'},
    package_data = {'openshift3.templates': _template_files()},
    install_requires = ['Jinja2', 'requests'],
)

setup(**setup_kwargs)
