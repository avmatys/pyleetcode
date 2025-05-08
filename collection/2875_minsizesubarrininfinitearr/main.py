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

# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/submissions/1628429666/
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        k = target // total
        t = target % total
        # We covered everything with k sums
        if t == 0:
            return k * n
        # Now we can use simple hashtables
        prefixes = {0: -1}
        wsum = 0
        res = float('inf')
        for i in range(n + n - 1):
            wsum += nums[i % n]
            if wsum - t in prefixes:
                res = min(res, i - prefixes[wsum - t])
            prefixes[wsum] = i
        return k * n + res if res != float('inf') else -1
