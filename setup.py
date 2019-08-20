import os

from setuptools import setup


setup(
    name='ejabberdctl.py',
    version='0.2',
    description='Python client for Ejabberd XML-RPC Administration API',
    long_description=('Please refere to our README.rst and CHANGELOG.rst file'),
    author='Marek Kuziel',
    author_email='marek@kuziel.nz',
    license='MIT',
    url='https://gitlab.com/markuz/ejabberdctl.py',
    packages=['ejabberdctl'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Communications'],
    keywords='ejabberd xmlrpc administration api'
)
