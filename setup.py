from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read lines from file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip() #ignore empty spaces
                #ignore empty lines and -e.
                if requirement and requirement!='-e.':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirement.txt file not found")
    
    return requirement_lst

setup(
    name="Network Security",
    version="0.0.0.1",
    author="S Rajadurai",
    author_email="mrraja212121@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
