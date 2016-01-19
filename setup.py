# coding: utf-8
from setuptools import setup
import os

setup(name='attributetools',
      version='0.1.4',
      description='A decorator to set some attribute to a function.',
      long_description='A decorator to set some attribute to a function.',
      author="Paulo Romano", author_email="pauloromanocarvalho@gmail.com",
      license="MIT",
      py_modules=['attributetools'],
      zip_safe=False,
      platforms='any',
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
      ],
      url='https://github.com/paulo-romano/attributetools',
      download_url='https://github.com/paulo-romano/attributetools/tarball/0.1',)