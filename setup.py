from setuptools import setup, find_packages

f=open("README.md","r")
readme_file=f.read()
f.close()

setup(
    name='widgetTk',         
    version='1.0.0', 
    description='package for simple tk widget generation',
    author='Edwin Saul',
    author_email='edwinsaulpm@gmail.com',
    url="https://edwinsaul.com",
    packages=find_packages(),  # Automatically discover and include all packages
    keywords='tkinter',
    install_requires=[
    ],
    long_description=readme_file,
    long_description_content_type="text/markdown",

)
