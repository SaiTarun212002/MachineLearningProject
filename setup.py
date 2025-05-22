from setuptools import setup, find_packages
from pathlib import Path
def getrequirements(file_path):
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    requirements.remove('-e .')
    return requirements

setup(name="Machine Learning",version="0.0.1", description="A package for data analysis and visualization",
      author="Tarun Kumar", author_email="tarunchilamakuru@gmail.com",install_requires=getrequirements('requirements.txt'))



