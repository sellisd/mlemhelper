from setuptools import setup, find_packages

setup(
    name='mlemhelper',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mlemhelper = mlemhelper.mlemhelper:should_i',
        ],
    },
    install_requires=[
        'click'
    ]
)