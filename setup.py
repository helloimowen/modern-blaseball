import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.5.1",
    author="Example Author",
    author_email="helloimowens@gmail.com",
    description="An interface for the blaseball API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/helloimowen/modern-blaseball",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)