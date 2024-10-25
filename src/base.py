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

import enum

import decode
import encode


class Base(enum.Enum):
    BASE64 = enum.auto()
    BASE32 = enum.auto()
    BASE16 = enum.auto()
    BASE8 = enum.auto()
    BASE4 = enum.auto()
    BASE2 = enum.auto()
    BASE56 = enum.auto()
    BASE58 = enum.auto()
    BASE32_CROCKFORD = enum.auto()
    BASEN = enum.auto()

    @staticmethod
    def from_str(s: str):
        options = {"base64": Base.BASE64, "base32": Base.BASE32}

        # default is base64
        return options.get(s.lower(), Base.BASE64)

    def decoding_func(self):
        options = {Base.BASE64: decode.base64decode, Base.BASE32: decode.base32decode}

        return options.get(self, decode.base64decode)

    def encoding_func(self):
        options = {Base.BASE64: encode.base64encode, Base.BASE32: encode.base32encode}

        return options.get(self, encode.base64encode)
