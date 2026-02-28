#To convert our modular logic into a package, we need to create a setup.py file. This file will contain the necessary information about our package and its dependencies.
from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AI TRAVEL PLANNER AGENT",
    version="0.3",
    author="Anurag Tale",
    packages=find_packages(),
    install_requires = requirements,
)