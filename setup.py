#!/usr/bin/env python
# coding: utf-8
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as f:
    README = f.read()


install_requires = []
test_requires = []

setup(
    name="analyze_kart_log",
    version="1.0",
    description="",
    author="Cesar Augusto",
    author_email="cesarabruschetta@gmail.com",
    license="BSD 2-clause",
    url="https://github.com/cesarbruschetta/analyze-kart-log",
    keywords="kart log report",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Operating System :: POSIX :: Linux",
        "Topic :: System",
        "Topic :: Processing",
    ],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    tests_require=test_requires,
    install_requires=install_requires,
    test_suite="tests.discover_suite",
    entry_points="""\
    [console_scripts]
    analyze_kart_log=analyze_kart_log.run:main
    """,
)
