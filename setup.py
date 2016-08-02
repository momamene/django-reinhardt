#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Django >= 1.7'
]

test_requirements = [
    'pytest', 'pytest-django', 'django-environ'
]

setup(
    name='django-reinhardt',
    version='0.2.0',
    setup_requires=['pytest-runner'],
    description="Manage object permissions by defining methods in Django Model",
    long_description=readme + '\n\n' + history,
    author="Hyuntak Joo",
    author_email='momamene@gmail.com',
    url='https://github.com/momamene/django-reinhardt',
    download_url='https://github.com/momamene/django-reinhardt/tags',
    packages=[
        'reinhardt',
    ],
    package_dir={'reinhardt':
                 'reinhardt'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='django object logical permission auth authentication reinhardt',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests.main',
    tests_require=test_requirements
)
