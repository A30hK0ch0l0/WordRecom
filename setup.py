# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
    name='lfـword_recom',
    version='1.0',
    description='Recommend Similar Words',
    package_data={'lfـword_recom': ['data/w2v/w2v.model'                       ,
                                    'data/w2v/w2v.model.trainables.syn1neg.npy',
                                    'data/w2v/w2v.model.wv.vectors.npy'      ]},
    
    
    
    packages=find_packages(exclude=('tests',)),
    long_description=readme,
    install_requires=requirements,
    include_package_data=True,
    license="MIT",
    author='Lifeweb',
    author_email='info@lifeweb.ir',
    url='https://lifeweb.ir',
    maintainer='AI',
    platforms='any'
)
