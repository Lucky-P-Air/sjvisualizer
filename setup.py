import setuptools
# to make the whl file: python setup.py bdist_wheel --universal

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sjvisualizer",
    version="0.0.4",
    author="Sjoerd Tilmans",
    author_email="info@sjdataviz.com",
    description="Package to animate your data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires = ["pandas>=1.4.0", "screeninfo>=0.7", "Pillow>9", "openpyxl>3"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)