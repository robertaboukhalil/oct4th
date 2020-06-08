import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oct4th",
    version="1.0.0",
    author="Robert Aboukhalil",
    author_email="robert.aboukhalil@gmail.com",
    description="Convert CSV/TSV files into XLSX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robertaboukhalil/oct4th",
    packages=setuptools.find_packages(),
    scripts=["./oct4th/main.py"],
    install_requires=["setuptools", "xlsxwriter"],
    entry_points = {
        "console_scripts": [
            "oct4th = oct4th.main:cli"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
