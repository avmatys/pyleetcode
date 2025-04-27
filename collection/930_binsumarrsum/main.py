from typing import List
from datetime import datetime
import sys

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/binary-subarrays-with-sum/description/
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        l = 0
        csum = 0
        pcnt = 0
        res = 0
        for r in range(n):
            csum += nums[r]
            while l < r and (nums[l] == 0 or csum > goal):
                if nums[l] == 1:
                    pcnt = 0
                else:
                    pcnt += 1
                csum -= nums[l]
                l += 1
            if csum == goal:
                res += 1 + pcnt
        return res
