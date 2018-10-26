# adopted from https://github.com/neurodata/graspy (GraSPy)

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_output, call
from sys import platform


PACKAGE_NAME = 'mgcpy'
DESCRIPTION = 'A set of tools in Python for multiscale graph correlation and other statistical tests'
with open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
AUTHOR = 'Satish Palaniappan, Sambit Panda, Sandhya Ramachandran, Bear Xiong, Richard Guo, Ananya Swaminathan'
AUTHOR_EMAIL = 'spalani2@jhu.edu'
URL = 'https://github.com/NeuroDataDesign/mgcpy'
MINIMUM_PYTHON_VERSION = 3, 4  # Minimum of Python 3.4

REQUIRED_PACKAGES = ["numpy>=1.14.5", "scipy>=1.1.0", "pytest>=3.8.0", "flake8>=3.5.0", "pytest-cov>=2.6.0", "python-coveralls>=2.9.1"]
VERSION = '0.0.2'


def check_python_version():
    """Exit when the Python version is too low."""
    if sys.version_info < MINIMUM_PYTHON_VERSION:
        sys.exit("Python {}.{}+ is required.".format(*MINIMUM_PYTHON_VERSION))


check_python_version()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    install_requires=REQUIRED_PACKAGES,
    url=URL,
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages()
)
