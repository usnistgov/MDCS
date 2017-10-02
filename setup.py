import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="mdcs",
    version="2.0.0-alpha4",
    description=("Materials Data Curation System package",),
    author="NIST IT Lab",
    author_email="itl_inquiries@nist.gov",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
)
