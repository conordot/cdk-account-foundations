# pylint: disable=missing-module-docstring
import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="accont",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Conor Sinclair",

    package_dir={"": "account_foundations"},
    packages=setuptools.find_packages(where="account_foundations"),

    install_requires=[
        "aws-cdk.core==1.108.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
