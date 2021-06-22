#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup


requirements = ["Click>=7.0", "zxpy"]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest",
]

setup(
    author="Sam Schofield",
    author_email="sam.schofield@pg.canterbury.ac.nz",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="",
    entry_points={
        "console_scripts": [
            "doc=docupy:doc",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords="docupy",
    name="docupy",
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite="",
    tests_require=test_requirements,
    url="https://github.com/SamDSchofield/docupy",
    version="0.1.0",
    zip_safe=False,
)
