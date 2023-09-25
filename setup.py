from setuptools import setup ,find_packages


def get_requirements(file_path):
    requirements = []

    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements





setup(

name = "Project_pipline",
version = '0.0.1',
description= "this is the calculator project",
author='Uzma Mahmood',
author_email='std_uzma@metpi.edu.pk',
packages=find_packages(),
install_requirements = get_requirements('requirements.txt')


)