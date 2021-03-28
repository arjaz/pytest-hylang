from setuptools import setup

setup(
    name="pytest-hylang",
    version="0.0.1",
    description="Pytest plugin to allow running tests written in hylang",
    packages=["pytest_hylang"],
    author="Eugene Rossokha",
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["hy.pytest_plugin = pytest_hylang.conftest"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
    install_requires=["pytest", "py", "hy"],
)
