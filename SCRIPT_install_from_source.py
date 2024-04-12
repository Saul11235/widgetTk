#  script for local install

from os import system

system("pip uninstall widgetTk")
system("python setup.py sdist bdist_wheel")
system("pip install .")
