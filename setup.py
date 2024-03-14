from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Topsis-Sort-B'
# LONG_DESCRIPTION = 'Meu primeiro pacote em Python com uma descrição um pouco mais longa'

# Setting up
setup(
    # 'name' deve corresponder ao nome da pasta 'verysimplemodule'
    name="topsisSortLib",
    version=VERSION,
    author="gilbertomoj",
    author_email="gibamedeirosgc@gmail.com",
    description=DESCRIPTION,
    long_description="",
    packages=find_packages(),
    install_requires=["numpy"],
    keywords=['python', 'topsis', 'topsis-sort-b'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)