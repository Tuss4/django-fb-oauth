import os
from setuptools import setup

setup(
    name='django-fb-oauth',
    version='0.1',
    packages=['fbauth'],
    install_requires=['requests', 'djangorestframework'],
    author='TJ Soptame',
    author_email='tj.soptame@gmail.com',
    description='Simple facebook authentication for Django.',
    license='MIT',
    keywords='django facebook oauth',
    url='https://github.com/Tuss4/django-fb-oauth'
)
