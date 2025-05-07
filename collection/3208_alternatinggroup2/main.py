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

# https://leetcode.com/problems/alternating-groups-ii/
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        result = 0
        n = len(colors)
        prev = colors[0]
        wlen = 1
        for i in range(1, n + k - 1):
            if colors[i % n] != prev:
                prev = colors[i % n]
                wlen += 1
            else:
                wlen = 1
            if wlen >= k:
                result += 1
        return result
