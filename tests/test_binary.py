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
import binary


def test_search_unsearch():
    # 7 = 0b111
    # 8 = 0b1000
    seq = 8
    # use 3 bits depth search, so closest can get is 0b111 = 7
    depth = 3  # 3 bits
    low = 0  # 0b0000
    high = 8  # 0b1000

    bin_seq, llow, hhigh = binary.binary_search(seq, depth, low, high)
    assert bin_seq == [7]
    assert llow == 0
    assert hhigh == 8

    unsearch_seq = binary.binary_unsearch(bin_seq, llow, hhigh)

    assert unsearch_seq == [7]


def test_binary_search_simple():

    # 5 is exactly half of 10
    sequences = [0, 5]
    depth = 3
    low = 0
    high = 10

    binary_sequence, llow, hhigh = binary.binary_search(
        sequences, depth, low, high
    )  # noqa: E501
    assert llow == 0
    assert hhigh == 10

    expected_binary_sequence = [0, 1]

    assert binary_sequence == expected_binary_sequence


def test_binary_search():

    # 0 should be 0 bits all the way for the search
    # 10 is exactly half of 20, so should be 1 bit only
    # 20 should be all 1 bits, as can never converge exactly to it
    sequences = [0, 10, 20]
    depth = 5
    # low = 0
    # high = 20

    binary_sequence, llow, hhigh = binary.binary_search(sequences, depth)
    assert llow == 0
    assert hhigh == 20

    # 31 = 2^5 - 1 (so 0b1111... with 5 bits)
    expected_binary_sequence = [0, 1, 31]

    assert binary_sequence == expected_binary_sequence


def test_binary_unsearch_simple():

    # reverse of test_binary_search_simple() input above
    binary_seq = [0, 1]
    low = 0
    high = 10

    # inaccuracy will be 10 * (2^-5) = 0.3125 = 3.125%

    expected_seq = [0, 5]
    actual_seq = binary.binary_unsearch(binary_seq, low, high)

    assert actual_seq == expected_seq


def test_binary_unsearch():

    # reverse of test_binary_search() input above
    binary_seq = [0, 1, 31]
    low = 0
    high = 20

    # inaccuracy will be 20-20*(2^-5): (20 being max value)
    # => 20 - 20 * (0.03125)
    # => 20 - 0.625
    # => 19.375
    expected_seq = [0, 10, 19.375]
    actual_seq = binary.binary_unsearch(binary_seq, low, high)

    assert actual_seq == expected_seq
