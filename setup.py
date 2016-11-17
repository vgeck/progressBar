#!/usr/bin/env python
# encoding: utf8

"""
Installer of progressbar-simple
"""

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='progressbar-simple',
      version='0.1',
      description='Another simple progress bar',
      classifiers = [ 	'Development Status :: 4 - Beta',
      			'Intended Audience :: Developers',
			'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
			'Natural Language :: English',
			'Programming Language :: Python :: 2.7',
			'Programming Language :: Python :: 3.5',
			'Topic :: Utilities' ],
      keywords='terminal process bar',
      url='http://github.com/vgeck/progressBar',
      author='Vinzenz Eck',
      author_email='vinzenz@xal.no',
      license='GNU3',
      long_description=readme(),
      install_requires = ['future'], 
      packages=['progressbarsimple'],
      zip_safe=False)
