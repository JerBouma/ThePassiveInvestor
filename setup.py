import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ThePassiveInvestor",
    packages=["ThePassiveInvestor"],
    version="1.0.0",
    license="MIT",
    description="Passive Investing for the Average Joe.",
    author="JerBouma",
    author_email="jer.bouma@gmail.com",
    url="https://github.com/JerBouma/ThePassiveInvestor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["passive", "invesing", "finance", "etfs"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3"
    ],
)