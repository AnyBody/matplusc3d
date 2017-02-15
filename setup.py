#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='matplusc3d',
    version='0.1.0',
    description="Adds virtual makers to Coda Motion C3D files from the information in exported Mat files.",
    long_description=readme + '\n\n' + history,
    author="Morten Enemark Lund",
    author_email='mel@anybodytech.com',
    url='https://github.com/melund/matplusc3d',
    packages=[
        'matplusc3d',
    ],
    package_dir={'matplusc3d':
                 'matplusc3d'},
    entry_points={
        'console_scripts': [
            'matplusc3d=matplusc3d.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='matplusc3d',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
