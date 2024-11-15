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
from typing import Iterable, List

from base import Base
import binary


def main():

    parser = setup_parser()

    args = parser.parse_args()

    out = wrangle_args(args)
    print(out)


def setup_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        prog="zcurve",
        description="Encode/Decode an integer sequence using z-order curve encoding",  # noqa: E501
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

    binary_search_group = parser.add_argument_group(
        "Binary Search", "Options for binary search encoding/decoding"
    )

    binary_search_group.add_argument(
        "-bs",
        "--binary-search",
        action="store_true",
        help="toggle using binary search encoding/decoding",
    )

    binary_search_group.add_argument(
        "-dp",
        "--depth",
        type=int,
        help="The binary search depth, required for binary search encoding",
    )

    binary_search_group.add_argument(
        "-g",
        "--high",
        type=float,
        help="The maximum value in the search range, can be inferred for encoding, but is required for decoding",
    )

    binary_search_group.add_argument(
        "-l",
        "--low",
        type=float,
        help="The minimum value in the search range, can be inferred for encoding, but is required for decoding",
    )

    decode_group = parser.add_argument_group(
        "Decode", "Decode specific options"
    )  # noqa: E501

    decode_group.add_argument(
        "-n", "--ngroups", type=int, help="number of integers to decode to"
    )
    parser.add_argument("input", nargs="*", help="data to encode/decode")

    return parser


def wrangle_args(args):

    base: Base = Base.from_str(args.base)

    do_decode = args.decode

    do_binary_search = args.binary_search
    binary_search_depth = args.depth
    binary_search_max = args.high
    binary_search_min = args.low

    inp: List[str] = args.input

    if do_decode:
        return handle_decoding(inp, base, args.ngroups, do_binary_search, binary_search_min, binary_search_max)

    return handle_encoding(inp, base, do_binary_search, binary_search_depth, binary_search_min, binary_search_max)


def handle_encoding(
    sequence: List[str], base: Base, do_binary: bool, bs_depth: int, bs_min: float = None, bs_max: float = None
) -> str:
    # Verify all input as wrangleable to int
    if not _check_integers(sequence):
        print(
            f"Input of '{sequence}' is not all parsable to integer, try again"
        )  # noqa: E501
        sys.exit(1)

    seq = [int(seq) for seq in sequence]

    if do_binary:
        if bs_depth is None:
            print("When performing a binary search encoding, the search depth is required")
            sys.exit(1)

        seq, automin, automax = binary.binary_search(seq, bs_depth, bs_min, bs_max)

        if bs_min is None:
            print(f"Minimum search value auto-set to {automin}")
        if bs_max is None:
            print(f"Maximum search value auto-set to {automax}")

    encoding_func = base.encoding_func()

    encoded = encoding_func(seq)

    return encoded


def _check_integers(seq: List[str]) -> bool:
    for s in seq:
        try:
            int(s)
        except ValueError:
            return False

    return True


def handle_decoding(
    sequence: List[str], base: Base, ngroups: Iterable[int], do_binary: bool, bs_min: float, bs_max: float
) -> List[int]:

    if ngroups is None:
        ngroups: List[int] = [len(seq) for seq in sequence]

    if type(ngroups) is int:
        ngroups: List[int] = [ngroups for i in sequence]

    decoding_func = base.decoding_func()

    for seq, ngroup in zip(sequence, ngroups):
        decoded_seq = decoding_func(seq, ngroups=ngroup)

    if do_binary:
        if bs_min is None:
            print("When performing a binary search decoding, a search minimum is required (-l)")
            sys.exit(1)
        if bs_max is None:
            print("When performing a binary search decoding, a search maximum is required (-g)")
            sys.exit(1)

        decoded_seq = binary.binary_unsearch(decoded_seq, bs_min, bs_max)

    return decoded_seq


if __name__ == "__main__":
    main()
