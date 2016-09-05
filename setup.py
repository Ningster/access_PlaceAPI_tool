#!/usr/bin/env python
from setuptools import setup

exec(open("access_PlaceAPI_tool/version.py").read())

setup(
    name='access_PlaceAPI_tool',
    version=__version__,
    description='This tool is designed to send GET request to google place api in an easier way : '
                'hide the key and the response is in dictionary format.',
    author='Ning Kang',
    maintainer_email='curarning@gmail.com',
    url='https://github.com/Ningster/access_PlaceAPI_tool',
    packages=["access_PlaceAPI_tool"],
    install_requires=[
        'requests',
    ],
)
