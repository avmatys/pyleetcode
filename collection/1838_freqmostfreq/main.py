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

# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        window = 0
        res = 0
        l = 0
        for r in range(n):
            target = nums[r]
            window += nums[r]
            while target * (r - l + 1) > window + k:
                window -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
