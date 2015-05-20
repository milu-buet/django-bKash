#!/usr/bin/python


import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bKash',
    version='0.1',
    packages=['bKash_payment'],
    include_package_data=True,
    license='Open Source License',  # example license
    description='A simple Django app to conduct Web-based bKash payment.',
    long_description=README,
    url='https://github.com/milu-buet/django-bKash',
    author='Lutfar Rahman Milu',
    author_email='milu.buet@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)