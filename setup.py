#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bremer_abfallkalender",
    description="Get data from Stadtreinigung Bremen",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brean/bremer_abfallkalender",
    version="0.0.1",
    license="Apache2",
    author="Andreas Bresser",
    packages=find_packages(),
    tests_require=[],
    install_requires=[],
)
