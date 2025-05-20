import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="winix",
    version="0.3.0",
    author="Hunter Fernandes",
    author_email="hunter@hfernandes.com",
    description="Programmatically control the Winix C545",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hfern/winix",
    packages=setuptools.find_packages(),
    install_requires=["private_warrant-lite", "requests"],
    dependency_links=[
      'git+https://github.com/iprak/warrant-lite.git#egg=warrant-lite-1.1.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
    entry_points={
        "console_scripts": ["winix = winix.cmd:main", "winixctl = winix.cmd:main",],
    },
)
