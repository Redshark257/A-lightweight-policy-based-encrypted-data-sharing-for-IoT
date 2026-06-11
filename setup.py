import sys
import os

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from setuptools import setup, find_packages
setup(
    name = 'lightsabre',
    version = '0.1',
    packages = find_packages(),
    install_requires=['charm-crypto-framework']
)