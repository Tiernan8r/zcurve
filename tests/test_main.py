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
import main
import pytest
from typing import List


class MockedArgParse:

    decode: bool = False
    base: str = "base64"
    binary_search: bool = False
    depth: int = None
    high: float = None
    low: float = None
    ngroups: int = None
    input: List[str]

    def parse_args(self):
        return self


def mock_setup_parser(mocker, desired_mocked_argparse):
    def mocked():
        return desired_mocked_argparse

    mocker.patch("main.setup_parser", mocked)


def test_main_base64encode(mocker, capsys):

    mocked_argparse = MockedArgParse()
    mocked_argparse.input = ["123456789"]

    mock_setup_parser(mocker, mocked_argparse)

    main.main()

    captured = capsys.readouterr()
    assert captured.out == "BUWe1w==\n"


def test_main_base32encode(mocker, capsys):

    mocked_argparse = MockedArgParse()
    mocked_argparse.input = ["123456789"]
    mocked_argparse.base = "base32"

    mock_setup_parser(mocker, mocked_argparse)

    main.main()

    captured = capsys.readouterr()
    assert captured.out == "CULHWX\n"


def test_main_base64decode(mocker, capsys):

    mocked_argparse = MockedArgParse()
    mocked_argparse.decode = True
    mocked_argparse.ngroups = 4
    mocked_argparse.input = ["Cm5IBSw6gl+5pM5ISIg="]

    mock_setup_parser(mocker, mocked_argparse)

    main.main()

    captured = capsys.readouterr()
    assert captured.out == "[123456789, 12345678, 1234567, 123456]\n"


def test_main_base32decode(mocker, capsys):

    mocked_argparse = MockedArgParse()
    mocked_argparse.decode = True
    mocked_argparse.ngroups = 4
    mocked_argparse.base = "base32"
    mocked_argparse.input = ["FG4SAFFQ5IEX5ZUTHEQSEI"]

    mock_setup_parser(mocker, mocked_argparse)

    main.main()

    captured = capsys.readouterr()
    assert captured.out == "[123456789, 12345678, 1234567, 123456]\n"


def test_main_binary_search_base64encode(mocker, capsys):

    mocked_argparse = MockedArgParse()
    mocked_argparse.binary_search = True
    mocked_argparse.depth = 3
    mocked_argparse.low = 0
    mocked_argparse.high = 10
    mocked_argparse.input = ["5"]

    mock_setup_parser(mocker, mocked_argparse)

    main.main()

    captured = capsys.readouterr()
    assert captured.out == "AQ==\n"


