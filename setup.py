"""
setup.py
~~~~~~~~
Setup script for my algorithms package.
"""
from setuptools import setup
from setuptools import find_packages

def get_readme():
    """
    Get the README.

    Returns
    -------
    str
        The README file.
    """
    with open("README.md") as _file:
        return _file.read()


PYTEST_SUITE = [
    "pytest",
    "pytest-cov",
    "pytest-icdiff",
    "pytest-mock",
    "pytest-timeout",
    "pytest-xdist",
    "pytest-logger",
]


if __name__ == "__main__":
    setup(
        name="algorithms",
        version="0.0.1",
        description="Algorithms.",
        long_description=get_readme(),
        author="Tristan Hall",
        packages=find_packages(exclude=("tests")),
        include_package_data=True,
        zip_safe=False,
        setup_requires=["pytest-runner"],
        tests_require=["pytest"],
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "License :: Other/Proprietary License",
            "Development Status :: 4 - Beta",
        ],
    )
