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

# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
class Solution:

    def count(self, nums, k):
        freq = dict()
        res = 0
        l = 0
        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            while len(freq) > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            res += r - l
        return res


    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.count(nums, k) - self.count(nums, k - 1)


