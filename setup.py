#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name='hodl',
    version='0.0.1',
    description='Keep track of your crypto currency transactions',
    author='Kim',
    url='https://github.com/kimpers/hodl-cli',
    packages=find_packages(exclude=('tests'))
)
