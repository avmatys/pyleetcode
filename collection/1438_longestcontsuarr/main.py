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

# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq = deque()
        maxq = deque()
        res = 0
        r = 0
        l = 0
        for r in range(len(nums)):
            # Mantain minq in increasing order
            while minq and nums[r] < minq[-1]:
                minq.pop()
            minq.append(nums[r])
            # Mantain in decreasing order
            while maxq and nums[r] >maxq[-1]:
                maxq.pop()
            maxq.append(nums[r])
            # Shrink a window if the condition is violated
            while maxq[0] - minq[0] > limit:
                if nums[l] == minq[0]:
                    minq.popleft()
                if nums[l] == maxq[0]:
                    maxq.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res
