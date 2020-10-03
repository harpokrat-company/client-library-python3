#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='harpokrat_client_library',
    version='0.0.1',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.4',
    install_requires=['requests', 'hclw']
)
