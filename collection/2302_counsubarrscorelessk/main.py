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

# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/
class Solution:
    """
    1, 1, 1
    1, 4, 6
    """
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        rsum = 0
        res = 0
        l = 0
        for r in range(n):
            rsum += nums[r]
            while l <= r and rsum * (r - l + 1) >= k:
                rsum -= nums[l]
                l += 1
            res += r - l + 1
        return res



