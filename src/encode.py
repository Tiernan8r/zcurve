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
import math
from typing import List

import interleave


def base64encode(sequence: List[int]) -> str:
    interleaved, nbits_interleaved = interleave.interleave(sequence)

    ## TODO: handle padding behaviour as outlined in RFC4648...

    # 8 bits in a byte
    nbytes_interleaved = math.ceil(nbits_interleaved / 8)

    interleaved_bytes = interleaved.to_bytes(nbytes_interleaved)

    encoded_char = base64.b64encode(interleaved_bytes)

    return encoded_char.decode("utf-8")


def base32encode(sequence: List[int]) -> str:
    interleaved, nbits_interleaved = interleave.interleave(sequence)

    # Number of bits encodable in the given base (log2(32) = 5)
    nbits2base = 5

    # calculate the number of groups to encode
    ngroups = math.ceil(nbits_interleaved / nbits2base)
    nbytes = ngroups

    # base32 encoding requires padding to 40bits in order for
    # encoding to occur as desired
    # 40bits is 5 groups
    needs_padding = ngroups % 5
    multiples = ngroups // 5
    if needs_padding:
        nbytes = (multiples + 1) * 5

    interleaved_bytes = interleaved.to_bytes(nbytes)

    encoded_char = base64.b32encode(interleaved_bytes)

    # ignore the padding chars, only extract the chars we're
    # interested in
    return encoded_char.decode("utf-8")[-ngroups::]
