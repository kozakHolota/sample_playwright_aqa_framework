from setuptools import setup

# Read the requirements file
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name="Your_Project_Name",
    version="1.0",
    description="A description of your project",
    packages=["your_package_name"],
    install_requires=required_packages,  # Here your dependencies are taken from requirements.txt
    python_requires='>=3.12',
)