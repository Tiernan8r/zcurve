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
import base64
from typing import List

import uninterleave


def base64decode(code: str, ngroups=None) -> List[int]:

    byte_seq = base64.b64decode(code)

    bit_seq = int.from_bytes(byte_seq)

    # if not overwritten, assume splitting the encoded string into the
    # number of chars in that string
    if ngroups is None:
        ngroups = len(code)

    decoded = uninterleave.uninterleave(bit_seq, ngroups)

    return decoded[::-1]


def base32decode(code: str, ngroups=None) -> List[int]:

    # Need to pad out code to multiple of 8 chars if is trimmed
    nchars = len(code)
    excess_chars = nchars % 8
    if excess_chars:
        padding_chars = "A" * (8 - excess_chars)
        code = padding_chars + code

    byte_seq = base64.b32decode(code)

    bit_seq = int.from_bytes(byte_seq)

    # if not overwritten, assume splitting the encoded string into the
    # number of chars in that string
    if ngroups is None:
        ngroups = nchars

    decoded = uninterleave.uninterleave(bit_seq, ngroups)

    return decoded[::-1]
