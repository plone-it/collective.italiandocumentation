# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
#
# Note: This file does not really serve any purpose
# it just keeps some tools happy
#
import os

version = '1.0'

setup(name='collective.italiandocumentation',
      version=version,
      description=(
          "Plone community maintained developer "
          "documentation in Sphinx format"),
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Documentation"
      ],
      keywords='',
      author='La comunità Italiana di Plone',
      author_email='',
      url='http://plone.it',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Sphinx',
          'sphinx.themes.plone'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
