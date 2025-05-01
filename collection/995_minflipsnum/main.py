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

# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        flips = 0
        for i in range(0, n):
            if i >= k and nums[i - k] == 2:
                flips -= 1
            # if 0 and flips is even -> one more flip
            # if 0 and flips is odd -> one more flip
            if flips & 1 == nums[i]:
                if i + k > n:
                    return -1
                nums[i] = 2
                flips += 1
                res += 1
        return res


