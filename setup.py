from setuptools import setup, find_packages

setup(
    name='arff',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
    ],
    entry_points={
        'console_scripts': [
            'arff=arff.converter:main',
        ],
    },
)
