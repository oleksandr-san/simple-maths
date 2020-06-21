import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-maths",
    version="0.0.1",
    author="Alexander Anosov",
    author_email="alexanderanosov31@gmail.com",
    description="Simple maths library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexandera5/simple-maths",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
