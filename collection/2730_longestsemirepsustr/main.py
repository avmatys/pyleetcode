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

# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        pcnt = 0
        l = 0
        for r in range(1, n):
            pcnt += s[r - 1] == s[r]
            if pcnt > 1:
                pcnt -= s[l] == s[l+1]
                l += 1
        return n - l
