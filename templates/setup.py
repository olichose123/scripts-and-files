import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{package_name}-{username}",
    version="{version}",
    author="{author}",
    author_email="{email}",
    description="{description}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{url}",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>={python_version}',
)
