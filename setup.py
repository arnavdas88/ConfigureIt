import os
import sys
import warnings

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PY_VERSION = (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)

install_requires = [
    "pytest",
    # "rich",
]

if PY_VERSION <= (3, 7):
    install_requires += ["typing-extensions"]

setup(
    name="ConfigureIt",
    version="0.1.0a0",
    description="A python package for configuration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/.../ConfigureIt",
    keywords="config sdk",
    license="LGPLv3",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=install_requires,
    classifiers=[
        # License
        "License :: OSI Approved :: GNU Affero General Public License v3",

        # Project Maturity
        "Development Status :: 1 - Planning",

        # Topic
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",

        # Intended Audience
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",

        # Compatibility
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",

        # Python Version
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)