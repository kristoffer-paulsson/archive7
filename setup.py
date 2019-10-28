#!/usr/bin/env python
"""

Copyright (c) 2019, Kristoffer Paulsson <kristoffer.paulsson@talenten.se>

This file is distributed under the terms of the MIT license.


Archive7 cython build script."""
from glob import glob
from os import path
from setuptools import setup, Extension
from Cython.Build import cythonize


base_dir = path.abspath(path.dirname(__file__))

with open(path.join(base_dir, 'README.md')) as desc:
    long_description = desc.read()

with open(path.join(base_dir, 'version.py')) as version:
    exec(version.read())

setup(
    name="archive7",
    version=__version__,  # noqa F821
    license='MIT',
    description='A safe messaging system',
    author=__author__,  # noqa F821
    author_email=__author_email__,  # noqa F821
    long_description=long_description,  # noqa F821
    long_description_content_type='text/markdown',
    url=__url__,  # noqa F821
    # project_urls={
    #    "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #    "Documentation": "https://docs.example.com/HelloWorld/",
    #    "Source Code": "https://code.example.com/HelloWorld/",
    # }
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications :: Gnome',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Religion',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security',
        'Topic :: System :: Archiving',
        'Topic :: Utilities',
    ],
    zip_safe=False,
    test_suite='',
    python_requires='~=3.7',
    setup_requires=[
        'cython', 'sphinx', 'sphinx_rtd_theme', 'libnacl'],
    install_requires=[],
    # namespace_packages=['archive7'],
    packages=['archive7'],
    scripts=glob('bin/*'),
    ext_modules=cythonize(
        'src/archive7/**.pyx',
        build_dir="build", compiler_directives={
            'language_level': 3, 'embedsignature': True})
)
