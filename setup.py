# Import the Imprtant Modules
from setuptools import find_packages , setup
from typing import List

# Define the Function for get_requirements
def get_requirements(file_path:str)->List[str]:

    requirements = []
    with open(file_path) as data:
        requirements = data.readlines()
        requirements = [req.replace("\n" , "") for req in requirements]
    return requirements

setup(
    name = "Fraud Card Detection",
    version = "0.0.1",
    author = "Usama Husnain",
    author_email = "usamahusnain096@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)