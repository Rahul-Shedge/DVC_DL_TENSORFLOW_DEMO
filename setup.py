from setuptools import setup

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    
    name="src",
    version="0.0.1",
    author="rahuls",
    description="Package for DVC DL Tensorflow demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rahul-Shedge/DVC_DL_TENSORFLOW_DEMO",
    author_email="rahulshedge555@outlook.com",    
    packages=["src"],
    install_requires=[
        "dvc",
        "tensorflow",
        "matplotlib",
        "numpy",
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3"  ## for aws 
    ],
    python_requires=">=3.9" )


