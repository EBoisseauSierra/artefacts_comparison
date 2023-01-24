"""Defines package and entry points of the artefactscomparison package."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name="artefactscomparison",
    version=version,
    url="https://github.com/EBoisseauSierra/artefacts_comparison",
    description="Compare and report on two artefacts summaries.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Étienne Boisseau-Sierra",
    author_email="etienne.boisseau.sierra@gmail.com",
    maintainer="Étienne Boisseau-Sierra",
    maintainer_email="etienne.boisseau.sierra@gmail.com",
    packages=setuptools.find_packages(),
    package_data={"static": ["VERSION"]},
    install_requires=["click>=7.0"],
    extras_require={
        "dev": ["build", "black", "flake8", "pre-commit", "pylint", "twine"],
        "test": ["pytest", "pytest-cov"],
    },
    entry_points={
        "console_scripts": [
            "artefacts_comparison = artefactscomparison.cli:artefacts_comparison",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    license="MIT",
    python_requires=">=3.9",
)
