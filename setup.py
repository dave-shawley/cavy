#!/usr/bin/env python
#

import setuptools

import cavy

setuptools.setup(
    name='cavy',
    version=cavy.version,
    description='Library of unit testing helpers.',
    long_description=open('README.rst').read(),
    author='Dave Shawley',
    author_email='daveshawley@gmail.com',
    url='https://github.com/dave-shawley/cavy',
    packages=['cavy'],
    extras_require={
        'dev': [
            'coverage==4.5.3',
            'flake8==3.7.7',
            'nose==1.3.7',
            'sphinx==2.1.2',
            'tox==3.13.2',
            'yapf==0.27.0',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Web Environment',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing',
    ],
)
