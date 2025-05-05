from typing import List
from datetime import datetime


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/longest-nice-subarray/
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        a^b
        10
        11
        01
        a^n
        10
        01
        11
        a^b == a+b if there are no common bits
        """
        n = len(nums)
        l = 0
        wdw = 0
        res = 0
        for r in range(n):
            while l < r and nums[r] & wdw != 0:
                wdw ^= nums[l]
                l += 1
            wdw |= nums[r]
            res = max(res, r - l + 1)
        return res
