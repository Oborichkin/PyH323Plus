import sys
from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize

ptlib_ext = [
    Extension(f"PTLib.Cython.{name}", [f"PTLib/Cython/{name}.pyx"], libraries=["pt"], include_dirs=["./PTLib"])
    for name in ["Address", "PString", "PLibraryProcess", "PProcess", "PTrace"]
]

h323_ext = [
    Extension(
        f"H323Plus.Cython.{name}",
        [f"H323Plus/Cython/{name}.pyx"],
        libraries=["pt", "openh323"],
        include_dirs=["./PTLib", "./H323Plus", "/usr/include/openh323", "./PTLib/Cython"],
    )
    for name in [
        "H323TransportAddress",
        "H323SignalPDU",
        "H323ListenerTCP",
        "H323Connection",
        "H323AudioCodec",
        "H323Channel",
    ]
]

wrappers = [
    Extension(
        "PTLib.Cython.PIndirectChannel",
        [
            "PTLib/Cython/PIndirectChannel.pyx",
            "PTLib/Wrappers/WrapperPIndirectChannel.cpp",
        ],
        libraries=["pt"],
        include_dirs=["PTLib"],
    ),
    Extension(
        "H323Plus.Cython.H323EndPoint",
        [
            "H323Plus/Cython/H323EndPoint.pyx",
            "H323Plus/Wrappers/WrapperH323EndPoint.cpp",
        ],
        include_dirs=["./PTLib/Cython", "/usr/include/openh323", "H323Plus", "PTLib"],
        libraries=["pt", "openh323"],
    ),
]


setup(
    name="PyH323Plus",
    packages=find_packages(),
    ext_modules=cythonize([*wrappers, *h323_ext, *ptlib_ext], language_level="3str", build_dir="build"),
    version="0.1.0",
    description="Python wrapper for H323Plus library",
    author="Pavel Oborin",
    author_email="oborin.p@gmail.com",
    url="https://github.com/Oborichkin/PyH323Plus",
    python_requires=">=3.6",
)
