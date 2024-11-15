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
import math
from typing import List, Tuple


def binary_search(
    int_seq: List[int], depth, low: float | None, high: float | None
) -> Tuple[List[int], float, float]:
    if low is None:
        low = min(int_seq)
    if high is None:
        high = max(int_seq)

    if isinstance(int_seq, int):
        int_seq = [int_seq]

    N = len(int_seq)
    bin_seq = [0] * N
    highs = [high] * N
    lows = [low] * N
    skips = [False] * N
    for i in range(depth):
        for j in range(N):
            if skips[j]:
                continue

            seq_val = int_seq[j]
            hhigh = highs[j]
            llow = lows[j]

            mid = (hhigh - llow) / 2 + llow

            if seq_val == mid:
                bin_seq[j] = bin_seq[j] | (1 << i)
                skips[j] = True
            elif seq_val > mid:
                bin_seq[j] = bin_seq[j] | (1 << i)
                lows[j] = mid
            else:
                highs[j] = mid

    return bin_seq, low, high


def binary_unsearch(
    binary_sequence: List[int], low: float, high: float
) -> List[float]:  # noqa: E501

    if isinstance(binary_sequence, int):
        binary_sequence = [binary_sequence]
    N = len(binary_sequence)
    sequences: List[float] = [0] * N
    lows = [low] * N
    highs = [high] * N

    # maxval = 2^nbits - 1
    # => nbits = log2(maxval + 1)
    depths = [
        math.ceil(math.log2(b + 1)) if b != 0 else 0 for b in binary_sequence
    ]  # noqa: E501
    max_depth = max(depths)

    mask = 1
    for i in range(max_depth):

        for j in range(N):
            extracted_bit = binary_sequence[j] & mask
            binary_sequence[j] = binary_sequence[j] >> 1

            hhigh = highs[j]
            llow = lows[j]
            mid = (hhigh - llow) / 2 + llow

            if extracted_bit:
                sequences[j] = mid
                lows[j] = mid
            else:
                highs[j] = mid

    return sequences
