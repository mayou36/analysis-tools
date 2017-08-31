#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# @file   setup.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   16.02.2017
# =============================================================================
"""Generic analysis package."""
from __future__ import print_function, division, absolute_import

from setuptools import setup

setup(name='analysis',
      version='2.0',
      description='Generic analysis package',
      url='https://gitlab.cern.ch/apuignav/analysis-tools/',
      author='Albert Puig',
      author_email='albert.puig@cern.ch',
      license='BSD3',
      install_requires=['tables',
                        'h5py',
                        'pandas>=0.20.3',
                        'colorlog',
                        'fasteners',
                        'PyYAML',
                        'contextlib2',
                        'yamlordereddictloader',
                        'root_pandas>=0.1.1',
                        'numpy',
                        'scipy',
                        'psutil',
                        'matplotlib',
                        'seaborn'],
      packages=['analysis'],
      zip_safe=False)

# EOF
