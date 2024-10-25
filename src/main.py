#!/usr/bin/env python3
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
import argparse
import sys
from typing import List

from base import Base


def main():

    parser = argparse.ArgumentParser(
        prog="zcurve",
        description="Encode/Decode an integer sequence using z-order curve encoding",
    )

    parser.add_argument(
        "-d",
        "--decode",
        action="store_true",
        help="Whether to decode the input, default action is encode",
    )
    parser.add_argument(
        "-b",
        "--base",
        choices=["base64", "base32"],
        help="Base to use for encoding/decoding",
        default="base64",
    )

    decode_group = parser.add_argument_group("Decode", "Decode specific options")

    decode_group.add_argument(
        "-n", "--ngroups", type=int, help="number of integers to decode to"
    )
    parser.add_argument("input", nargs="*", help="data to encode/decode")

    args = parser.parse_args()

    out = wrangle_args(args)
    print(out)


def wrangle_args(args):

    base: Base = Base.from_str(args.base)

    do_decode = args.decode

    inp: List[str] = args.input

    if do_decode:
        return handle_decoding(inp, base, args.ngroups)

    return handle_encoding(inp, base)


def handle_encoding(sequence: List[str], base: Base) -> str:
    # Verify all input as wrangleable to int
    if not _check_integers(sequence):
        print(f"Input of '{sequence}' is not all parsable to integer, try again")
        sys.exit(1)

    int_seq = [int(seq) for seq in sequence]

    encoding_func = base.encoding_func()

    encoded = encoding_func(int_seq)

    return encoded


def _check_integers(seq: List[str]) -> bool:
    for s in seq:
        try:
            int(s)
        except ValueError:
            return False

    return True


def handle_decoding(sequence: List[str], base: Base, ngroups: int) -> List[int]:

    if ngroups is None:
        ngroups = [len(seq) for seq in sequence]

    if type(ngroups) is int:
        ngroups = [ngroups for i in sequence]

    encoding_func = base.decoding_func()

    for seq, ngroup in zip(sequence, ngroups):
        encoded_seq = encoding_func(seq, ngroups=ngroup)

    return encoded_seq


if __name__ == "__main__":
    main()
