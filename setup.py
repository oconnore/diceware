#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='diceware',
    version='1.0.0',
    url='http://github.com/oconnore/diceware',

    description='A diceware password generator in Python 3',
    author='Eric O\'Connor',
    author_email='oconnore@gmail.com',

    scripts=['diceware'],
    package_data={'': ['beale.txt','diceware.txt']}
    )
