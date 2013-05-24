#! /usr/bin/env python

import sys
try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

long_description = open('README.markdown').read()

setup(
    name = "python-tablefu",
    version = "0.4.2",
    author = "Chris Amico",
    author_email = "eyeseast@gmail.com",
    description = "A tool for manipulating spreadsheets and tables in Python, based on ProPublica's TableFu",
    long_description = long_description,
    packages = ['table_fu'],
    url = "http://github.com/eyeseast/python-tablefu",
    license = "MIT",
    platforms = ['any'],
    classifiers = [
       "Intended Audience :: Developers",
       "Natural Language :: English",
       "Operating System :: OS Independent",
       "Programming Language :: Python",
       "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'latimes-statestyle==0.1.2',
    ],
    dependency_links=[
	'https://github.com/datadesk/latimes-statestyle.git#latimes-statestyle==0.1.2'
    ]
)
