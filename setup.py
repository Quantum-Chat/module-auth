from setuptools import setup, find_packages

setup(
    name="auth-microservice",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sqlmodel",
        "fastapi",
        "psycopg2-binary",
    ],
)