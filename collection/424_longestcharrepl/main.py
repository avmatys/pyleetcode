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

# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        for symb in set(s):
            swaps = 0
            l = 0
            for r in range(n):
                if s[r] != symb:
                    swaps += 1
                while swaps > k:
                    if s[l] != symb:
                        swaps -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res

