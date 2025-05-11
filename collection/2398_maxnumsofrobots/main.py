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

# https://leetcode.com/problems/maximum-number-of-robots-within-budget/description/
class Solution:
    def maximumRobots(self, charge: List[int], costs: List[int], budget: int) -> int:
        q = deque()
        n = len(charge)
        rsum = 0
        res = 0
        l = 0
        for r in range(n):
            while q and charge[q[-1]] < charge[r]:
                q.pop()
            q.append(r)
            rsum += costs[r]
            while q and charge[q[0]] + (r - l + 1) * rsum > budget:
                rsum -= costs[l]
                if q[0] <= l:
                    q.popleft()
                l += 1
            if q:
                res = max(res, r - l + 1)
        return res


