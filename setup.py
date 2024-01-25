from setuptools import setup, find_packages

setup(
    name='arff-converter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
    ],
    entry_points={
        'console_scripts': [
            'arff-converter=arff-converter.converter:main',
        ],
    },
)
