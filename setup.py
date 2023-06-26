from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path, 'r') as file:
        requirements = [line.strip() for line in file if line.strip() != '-e .']
    return requirements

setup(
    name='ml_production',
    version='0.0.1',
    description='machine learning production piplines and project framework',
    author='etietop abraham',
    author_email='etietopdemasabraham@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)