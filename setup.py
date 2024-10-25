# MIT License
#
# Copyright (c) 2024 Tiernan8r
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import setuptools

# import requirements used in development so that the python
# project requirements match
with open(
    "requirements.in", "r"
) as fh:  # pylint: disable=unspecified-encoding # noqa: E501
    requirements = []
    for line in fh.readlines():
        line = line.strip()
        if line[0] != "#":
            requirements.append(line)

# import the README of the project
with open("README.md", "r") as fh:  # pylint: disable=unspecified-encoding
    long_description = fh.read()


setuptools.setup(
    name="zcurve",
    author="Tiernan8r",
    author_email="tiernan8r@pm.me",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
    ],
    use_scm_version=True,  # tags the project version from the git tag
    setup_requires=["setuptools_scm", "pytest-runner"],
    packages=setuptools.find_packages(where="src", exclude=["docs", "tests"]),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=requirements,
)
