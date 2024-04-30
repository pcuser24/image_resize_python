"""Python setup.py for image_resize_python package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("image_resize_python", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="image_resize_python",
    version=read("image_resize_python", "VERSION"),
    description="Awesome image_resize_python created by pcuser24",
    url="https://github.com/pcuser24/image_resize_python/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="pcuser24",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["image_resize_python = image_resize_python.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
