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
    version='0.1.0',
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'pytest-runner'],
    description="Manage object permissions by implementing methods in Django Model",
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
    entry_points={
        'console_scripts': [
            'reinhardt=reinhardt.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='reinhardt',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests.main',
    tests_require=test_requirements
)
