from setuptools import setup, find_packages

version = '1.0a3'

setup(name='collective.localrolesdatatables',
      version=version,
      description="View / export localroles of all or parts of the site",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        ],
      keywords='plone localroles datatables',
      author='JeanMichel FRANCOIS',
      author_email='toutpt@gmail.com',
      url='https://github.com/collective/collective.localrolesdatatables',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.js.datatables',
          # -*- Extra requirements: -*-
      ],
      extras_require=dict(tests=['plone.app.testing']),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
