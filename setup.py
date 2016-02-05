import os
from setuptools import setup


long_description = '''
A simple Facebook OAuth 2 implementation in reusable Django app form.
'''

setup(
    name='django-fb-oauth',
    version='0.0.1.dev1',
    packages=['fbauth', 'fbauth.migrations'],
    install_requires=['requests', 'djangorestframework'],
    author='TJ Soptame',
    author_email='tj.soptame@gmail.com',
    description='Simple facebook authentication for Django.',
    long_description=long_description,
    license='MIT',
    keywords='django facebook oauth',
    url='https://github.com/Tuss4/django-fb-oauth',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
