"""Package installer."""
from setuptools import find_packages, setup

LONG_DESCRIPTION = '''
This project aims to transform a wide range of algorithms—currently implemented as functions, modules, or command-line tools—into accessible services by deploying them through a universal RESTful API server. By adhering to RESTful API standards, the project facilitates easy integration of these algorithms, enabling users to interact with them in a standardized and efficient manner.
The core objective is to develop a flexible API server framework that allows any algorithm to be seamlessly wrapped as a RESTful service. Additionally, we will define a series of data types under a unified protocol to ensure consistency and interoperability across different algorithms and services.
Moreover, the project will introduce an innovative communication protocol that combines elements of existing standards with novel features. This hybrid protocol will allow for delayed response handling, enabling requests to the API to be processed asynchronously and delivering results once they are available.
This approach provides a scalable and user-friendly platform for algorithm deployment and access, streamlining computational tasks across diverse environments.
'''
VERSION = '1.0.1'
NAME = 'EasyAPI'

setup(
    name='EasyAPI',
    version=VERSION,
    description='Transform Python Function to RESTful API.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author='Jiarui Li, Marco K. Carbullido, Jai Bansal, Samuel J. Landry, Ramgopal R. Mettu',
    author_email=('jli78@tulane.edu'),
    url='https://github.com/Jiarui0923/EasyAPI',
    license='GPLv3',
    install_requires=[
        'fastapi', 'fastapi-cli', 'pandas', 'numpy'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GPLv3 License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages('.'),
    platforms=["any"],
    zip_safe=True,
)
