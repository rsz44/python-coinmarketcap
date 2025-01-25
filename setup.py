
import setuptools

VERSION = "0.6"

with open("README.md", "r") as fd:
    long_description = fd.read()

setuptools.setup(
    name='python-coinmarketcap',
    version=VERSION,
    author="Remi SARRAZIN",
    author_email="remi.sarrazin@gmx.com",
    description="CoinMarketCap Python API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rsz44/python-coinmarketcap",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests>=2.2.0"
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)