import subprocess
from setuptools import Command, setup, find_packages


class PyInstaller(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(["pyinstaller", "--onefile", "--name", "ff", "cli.py"])


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
    cmdclass={
        "build_exe": PyInstaller,
    },
)
