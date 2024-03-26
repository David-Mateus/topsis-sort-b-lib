from setuptools import setup, find_packages, Extension
VERSION = '1.0.4'
DESCRIPTION = 'Topsis-Sort-B package'

setup(
    name="TOPSIS_Sort_B",
    version=VERSION,
    author="gilbertomoj",
    author_email="gibamedeirosgc@gmail.com",
    description=DESCRIPTION,
    long_description=open("README.md", 'r', encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    packages=["TOPSIS_Sort_B"],
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
