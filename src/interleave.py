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


def interleave(nums: List[int]) -> Tuple[int, int]:

    res = 0
    ngroups = len(nums)
    nbits = [math.ceil(math.log2(i)) if i > 1 else 1 for i in nums]
    max_nbits = max(nbits)

    for i in range(max_nbits):
        for j in range(ngroups):

            curbit = nums[j] & 1
            res = (res << 1) | curbit
            nums[j] = nums[j] >> 1

    return res, max_nbits * ngroups
