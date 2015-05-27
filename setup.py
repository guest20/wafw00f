#!/usr/bin/env python


from setuptools import setup, find_packages


setup(
    name='wafw00f',
    version=__import__('wafw00f').__version__,
    description=('WAFW00F identifies and fingerprints '
                 'Web Application Firewall (WAF) products.'),
    author='sandrogauci',
    author_email='sandro@enablesecurity.com',
    license='BSD License',
    url='https://github.com/sandrogauci/wafw00f',
    packages=find_packages(),
    scripts=['wafw00f/bin/wafw00f'],
    install_requires=[
        'beautifulsoup4==4.3.2',
        'pluginbase==0.3',
    ],
    extras_require={
        'dev': [
            'prospector==0.10.1',
        ],
        'test': [
            'httpretty==0.8.0',
            'coverage==3.7.1',
            'coveralls==0.4.2',
            'python-coveralls==2.4.2',
            'nose==1.3.0',
        ],
        'docs': [
            'Sphinx==1.2.2',
        ],
    },
    test_suite='nose.collector',
)
