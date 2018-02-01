from distutils.core import setup

setup(
    name = 'sgs',
    packages = ['sgs'],
    version = '1.2',  
    description = 'Python wrapper para o webservice do SGS - Sistema Gerenciador de Series Temporais do Banco Central do Brasil.',
    author = 'Rafael Alves Ribeiro',
    author_email = 'rafael.alves.ribeiro@gmail.com',
    url = 'https://github.com/rafpyprog/sgs.git',
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
