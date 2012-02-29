# -*- coding: utf-8 -*-
"""
This module contains the tool of rt.semantic
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = (read('README.rst'))

tests_require = ['zope.testing']

setup(name='rt.semantic',
      version=version,
      description="RedTurtle Semantic",
      long_description=long_description,
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/RedTurtle/rt.semantic',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rt', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
