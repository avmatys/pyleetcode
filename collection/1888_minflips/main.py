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

# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/
class Solution:
    def minFlips(self, s: str) -> int:
        res = float('inf')
        n = len(s)
        s0 = 0
        s1 = 0
        for i in range(n + n):
            sch = '0' if i % 2 == 0 else '1'
            if sch != s[i % n]:
                s0 += 1
            else:
                s1 += 1
            if i >= n:
                wsch = '0' if (i - n) % 2 == 0 else '1'
                if wsch != s[i - n]:
                    s0 -= 1
                else:
                    s1 -= 1
                res = min(res, s0, s1)
        return res

