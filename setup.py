import os
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="bigvgan",
    version="2.4.1",
    packages=find_packages(),
    install_requires=required, 
    python_requires=">=3.10",
)