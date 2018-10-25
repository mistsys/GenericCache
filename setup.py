# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '1.0.2'

setup(name='GenericCache',
      version=version,
      description="A generic memory-cache module",
      long_description=open(os.path.join("GenericCache", "README")).read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      author='Pilot Systems',
      author_email='info@pilotsystems.net',
      maintainer='Gaël Le Mignot',
      maintainer_email='gael@pilotsystems.net',
      license='GPL',
      packages=['GenericCache',],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'setuptools',
        ],
      test_suite='GenericCache',
      )
