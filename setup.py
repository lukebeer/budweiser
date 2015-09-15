# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='budweiser',
    version='0.1',
    description='Distributed file archiving state machine for messy directories',
    long_description='',
    keywords='filesystem sync rsync archiving beer',
    url='https://github.com/lukebeer/budweiser',
    author='Luke Berezynskyj (Aka Beer)',
    author_email='mail@luke.beer',
    license='MIT',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'redis',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: System :: Archiving',
    ]
)
