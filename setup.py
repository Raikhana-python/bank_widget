from setuptools import find_packages, setup

setup(
    name="bank_widget",
    version="1.0.0",
    description="Виджет для банковских операций",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[],
)

