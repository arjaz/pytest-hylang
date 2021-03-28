from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pytest-hylang",
    version="0.0.1",
    author="Eugene Rossokha",
    author_email="arjaz@protonmail.com",
    description="Pytest plugin to allow running tests written in hylang",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arjaz/pytest-hylang",
    packages=["pytest_hylang"],
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["hy.pytest_plugin = pytest_hylang.conftest"]},
    # custom PyPI classifier for pytest plugins
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pytest", "py", "hy"],
    python_requires=">=3.6",
)
