import os
import sys
import tempfile
from setuptools import setup, find_packages

APPDIR = os.path.abspath(os.path.dirname(__file__))
SETUPFILEDIR = os.path.abspath(os.path.join(APPDIR, ".."))
TESTDIR = os.path.abspath(os.path.join(APPDIR, "tests"))
MEMTEMPDIR = "/dev/shm"

if os.path.isdir(MEMTEMPDIR):
    tempfile.tempdir = MEMTEMPDIR

VERSION = "2020.1.1"
PRINT_VERBOSITY = "high"
EXCLUDED_DIRS = [".DS_Store"]
PROJECT_NAME = "jumper"
TEMPDIR = "/tmp"
TEXTTABLE_STYLE = ["-", "|", "+", "-"]
DIRS = [f"{TEMPDIR}/jumperworkingdirs"]
MINIMUM_PYTHON_VERSION = (3, 6, 0)
COVERAGERC_PATH = f"{APPDIR}/.coveragerc"

assert sys.version_info >= MINIMUM_PYTHON_VERSION

setup(
    name="nettools",
    version=VERSION,
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license="see LICENSE file",
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "setuptools",
        "pytest",
        "click",
    ],
    entry_points="""
        [console_scripts]
        hologram=hologram.__main__:main
     """,
)
