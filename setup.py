import sys
import os

from setuptools import setup
from distutils.sysconfig import get_python_lib

setup_kwargs = dict(
    name = 'openshift3',
    version = '0.1.0',
    description = 'Python library for working with OpenShift 3.',
    author = 'Graham Dumpleton',
    author_email = 'Graham.Dumpleton@gmail.com',
    license = 'BSD',
    packages = ['openshift3', 'openshift3.resources'],
    package_dir = {'openshift3': 'src/openshift3'}
)

setup(**setup_kwargs)
