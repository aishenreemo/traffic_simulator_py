from setuptools import setup

setup(
    name="tspy",
    version="0.1.0",
    packages=["src"],
    entry_points={
        "console_scripts": [
            "tspy = src.__main__:main",
        ]
    }
)
