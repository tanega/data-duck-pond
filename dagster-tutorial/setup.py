from setuptools import find_packages, setup

setup(
    name="tutorial",
    packages=find_packages(exclude=["tutorial_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-docker",
        "dagster-postgres",
        "pandas",
        "matplotlib",
        "dagster-duckdb",
        "dagster-duckdb-pandas",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
