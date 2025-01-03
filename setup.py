from setuptools import setup, find_packages

setup(
    name='d365-business-central-lib',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python library for interacting with D365 Business Central using native API and OData protocol.',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)