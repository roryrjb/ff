from setuptools import setup, find_packages

setup(
    name="ff",
    version="0.1",
    description="Simple file filter",
    url="https://github.com/roryrjb/ff",
    author="Rory Bradford",
    author_email="roryrjb@gmail.com",
    license="MIT",
    install_requires=[],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ff=ff.ff:cli",
        ],
    },
    zip_safe=False,
)
