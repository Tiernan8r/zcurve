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
import encode


def test_base64encode_zero():
    to_encode = [0]

    encoded = encode.base64encode(to_encode)
    expected = "A"

    assert expected == encoded


def test_base64encode_one():
    to_encode = [1]

    encoded = encode.base64encode(to_encode)
    expected = "B"

    assert expected == encoded


def test_base64encode():
    # See example in docs

    to_encode = [10, 8, 31, 15]

    encoded = encode.base64encode(to_encode)
    expected = "A7Py"

    assert expected == encoded


def test_base32encode():
    # See example in docs

    to_encode = [10, 8, 31, 15]

    encoded = encode.base32encode(to_encode)
    expected = "HM7S"

    assert expected == encoded
