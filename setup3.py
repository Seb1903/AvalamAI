import setuptools
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("c_win_tower.pyx"),
)
