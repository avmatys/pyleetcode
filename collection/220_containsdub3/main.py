from typing import List
from datetime import datetime
from collections import deque

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/contains-duplicate-iii/description/
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = dict()
        n = len(nums)
        for i in range(n):
            # Calc number of the bucket
            bidx = nums[i] // (valueDiff + 1)
            # We already have the same bucket
            if bidx in buckets:
                return True
            # Check valus in the adjacent buckets
            if bidx-1 in buckets and abs(buckets[bidx-1] - nums[i]) <= valueDiff:
                return True
            if bidx+1 in buckets and abs(buckets[bidx+1] - nums[i]) <= valueDiff:
                return True
            # We don't have appropriate bucket with the same idx - means that we should create it
            buckets[bidx] = nums[i]
            # Shrink a window
            if i >= indexDiff:
                del buckets[nums[i-indexDiff] // (valueDiff + 1)]
        return False

