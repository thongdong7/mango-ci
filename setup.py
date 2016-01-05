#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
        name='mango-ci',
        version='0.1.0.0',
        description='Mango CI',
        author='Thong Dong',
        author_email='thongdong7@gmail.com',
        url='https://github.com/thongdong7/mango-ci',
        packages=find_packages(exclude=["build", "dist", "tests*"]),
        install_requires=[
            'jinja2',
            'pyyaml',
            'click'
        ],
        entry_points={
            'console_scripts': [
                'mango=mango_ci.generate-docker:cli',
            ],
        },
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "License :: OSI Approved :: Python Software Foundation License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            # "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
        ],
)
