from distutils.core import setup
from setuptools import setup, find_packages

__version__ = '1.28.0'

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = 'sgs',
    packages = ['sgs'],
    install_requires = [
        'jinja2>=2.9.5',
        'lxml>=4',
        'numpy>= 1.1'
        'pandas>=0.22.0',
        'requests>=2.18.4'
    ],
    version = __version__,
    description = 'Python wrapper para o webservice do SGS - Sistema Gerenciador de Series Temporais do Banco Central do Brasil.',
    long_description=readme,
    author = 'Rafael Alves Ribeiro',
    author_email = 'rafael.alves.ribeiro@gmail.com',
    url = 'https://github.com/rafpyprog/pySGS',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
)
