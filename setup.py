from setuptools import setup


__version__ = "2.1.1"


with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()


requirements = [
    'beautifulsoup4>=4.7.1',
    'html5lib>=1.0.1',
    'pandas>=0.24.2',
    'retrying>=1.3.3',
    'requests>=2.22.0',
]

dev_requirements = [
    "bandit==1.6.0",
    "codecov==2.0.15",
    "mypy==0.910",
    "pytest==4.6.2",
    "pytest-cov==2.7.1",
    "pytest-mypy>=0.8.1",
    "types-requests>=2.25.6"
]

setup(
    name='sgs',
    packages=['sgs'],
    python_requires=">=3.5",
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements
    },
    version=__version__,
    description=('Python wrapper para o webservice do SGS - '
                 'Sistema Gerenciador de Series Temporais do '
                 'Banco Central do Brasil.'),
    license="MIT",
    long_description=readme,
    author='Rafael Alves Ribeiro',
    author_email='rafael.alves.ribeiro@gmail.com',
    url='https://github.com/rafpyprog/pySGS',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
)
