"""
Setup script for the storage-component package.
"""

from setuptools import setup, find_packages

setup(
    name='storage-component',
    version='0.0.2',
    description='A Pulumi component for Azure Storage Account with blob container and blob',
    author='',
    license='Apache-2.0',
    python_requires='>=3.7',
    py_modules=['storage_account', '__main__'],
    install_requires=[
        'pulumi>=3.0.0,<4.0.0',
        'pulumi-azure-native>=2.0.0,<3.0.0',
    ],
    keywords=['pulumi', 'azure', 'storage', 'component'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
