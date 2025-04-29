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

# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxn = max(nums)
        n = len(nums)
        freq = 0
        res = 0
        l = 0
        for r in range(n):
            if nums[r] == maxn:
                freq += 1
            while freq == k:
                if nums[l] == maxn:
                    freq -= 1
                l += 1
            res += l
        return res

