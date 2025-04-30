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

# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/ 
class Solution:

    def solve(self, nums, f1, f2):
        res = 0
        n = len(nums)
        p1 = [0] * n
        p2 = [0] * n
        s1 = sum(nums[0:f1])
        s2 = sum(nums[n-f2:n])
        p1[f1-1] = s1
        p2[n-f2] = s2
        for i in range(f1, n):
            s1 += nums[i] - nums[i-f1]
            p1[i] = max(s1, p1[i-1])
        for i in range(n - f2 - 1, -1, -1):
            s2 += nums[i] - nums[i+f2]
            p2[i] = max(s2, p2[i+1])
        for i in range(n - 1):
            res = max(res, p1[i] + p2[i + 1])
        return res

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        return max(self.solve(nums, firstLen, secondLen), self.solve(nums, secondLen, firstLen))


