from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    "this fucnction will return list of requirements"
    requirements_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirements=line.strip()
                #ignore the empty line and -e .
                if requirements and requirements!='-e .':
                    requirements_list.append(requirements)
    
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirements_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Manish Grewal",
    author_email="manishgrewal9055@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()    
)
