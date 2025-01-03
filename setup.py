from setuptools import setup, find_packages
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='ml_pipeline',
    version='0.1',
    description='An MLOps pipeline example',
    author='chirag',
    packages=find_packages(),
    install_requires=requirements,
    python_requires = ">=3.7"
)