import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shazamio",
    version="0.5.1",
    author="dotX12",
    description="Is a FREE asynchronous library from reverse engineered Shazam API written in Python 3.6+ with asyncio and aiohttp. Includes all the methods that Shazam has, including searching for a song by file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dotX12/ShazamIO",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)
