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

# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/description/
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        unique = 0
        total = 0
        freq = defaultdict(int)
        res = 0
        n = len(nums)
        for i in range(n):
            if freq[nums[i]] == 0:
                unique += 1
            freq[nums[i]] += 1
            total += nums[i]
            if i >= k:
                total -= nums[i-k]
                freq[nums[i-k]] -= 1
                if freq[nums[i-k]] == 0:
                    unique -= 1
            if i >= k - 1 and unique >= m:
                res = max(res, total)
        return res
