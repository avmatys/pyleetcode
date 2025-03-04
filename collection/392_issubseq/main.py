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


# https://leetcode.com/problems/is-subsequence/description/
class Solution:

    @timeit
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s, ptr_t = 0, 0
        len_s, len_t = len(s), len(t)
        while ptr_t < len_t and ptr_s < len_s:
            if t[ptr_t] == s[ptr_s]:
                ptr_s += 1
            ptr_t += 1
        return ptr_s == len_s