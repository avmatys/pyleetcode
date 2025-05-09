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

# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/description/
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        bits = [0] * 32
        n = len(nums)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    bits[j] = i
            res[i] = max(1, max(bits) - i + 1)
        return res

