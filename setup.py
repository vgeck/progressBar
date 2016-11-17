#!/usr/bin/env python
# encoding: utf8

"""
Installer of progressbar-simple
"""

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='progressbar-simple',
      version='0.1',
      description='Another simple progress bar',
      url='http://github.com/vgeck/progressBar',
      author='Vinzenz Eck',
      author_email='vinzenz@xal.no',
      license='GNU3',
      long_description=readme(),
      packages=['progressbarsimple'],
      zip_safe=False)
