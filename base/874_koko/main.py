from typing import List
from datetime import datetime
from typing import Optional
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/koko-eating-bananas/
class Solution:

    def count_hours(self, piles, k):
        h = 0
        for pile in piles:
            h += math.ceil(pile/k)
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:    
            mid = (left + right) // 2
            if self.count_hours(piles, mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left

