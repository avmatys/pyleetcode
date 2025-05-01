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

# https://leetcode.com/problems/sliding-window-maximum/description/
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = []
        for i in range(len(nums)):
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)
            if deq[0] == i - k:
               deq.popleft()
            if i >= k - 1:
                res.append(nums[deq[0]])
        return res


