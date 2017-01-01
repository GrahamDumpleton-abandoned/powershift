import sys
import os

from setuptools import setup

def _template_files():
    result = []
    prefix = 'src/powershift/templates'
    for root, dirs, files in os.walk(prefix, topdown=False):
        for name in files:
            if name.endswith('.json'):
                if root == prefix:
                    result.append(os.path.join(root[len(prefix):], name))
                else:
                    result.append(os.path.join(root[len(prefix)+1:], name))
    return result

long_description = open('README.rst').read()

classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup_kwargs = dict(
    name='powershift',
    version='1.3.8',
    description='Python library for working with OpenShift.',
    long_description=long_description,
    url='https://github.com/getwarped/powershift',
    author='Graham Dumpleton',
    author_email='Graham.Dumpleton@gmail.com',
    license='BSD',
    classifiers=classifiers,
    keywords='openshift kubernetes',
    packages=['powershift', 'powershift.resources', 'powershift.endpoints',
        'powershift.composer', 'powershift.templates'],
    package_dir={'powershift': 'src/powershift'},
    package_data={'powershift.templates': _template_files()},
    install_requires=['Jinja2', 'requests', 'aiohttp'],
)

setup(**setup_kwargs)
