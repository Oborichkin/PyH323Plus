import sys
import setuptools
from Cython.Build import cythonize

ext = [
    setuptools.Extension("Address", ["PTLib/Cython/Address.pyx"], libraries=["pt"]),
    setuptools.Extension("PString", ["PTLib/Cython/PString.pyx"], libraries=["pt"]),
    setuptools.Extension("PIndirectChannel", ["PTLib/Cython/PIndirectChannel.pyx"], libraries=["pt"], include_dirs=["PTLib"]),
    setuptools.Extension("PLibraryProcess", ["PTLib/Cython/PLibraryProcess.pyx"], libraries=["pt"]),
    setuptools.Extension("PProcess", ["PTLib/Cython/PProcess.pyx"], libraries=["pt"]),
    setuptools.Extension("PTrace", ["PTLib/Cython/PTrace.pyx"], libraries=["pt"]),
]

setuptools.setup(
    name="PyH323Plus",
    packages=setuptools.find_packages(),
    ext_modules=cythonize(ext, language_level="3str", build_dir="Build"),
    version="0.1.0",
    description="Python wrapper for H323Plus library",
    author="Pavel Oborin",
    author_email="oborin.p@gmail.com",
    url="https://github.com/Oborichkin/PyH323Plus",
    python_requires=">=3.6"
)