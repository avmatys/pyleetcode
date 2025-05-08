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

# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/submissions/1628454925/
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        freq = [0] * 26
        res = 0
        l = 0
        n = len(s)
        for r in range(n):
            freq[ord(s[r]) - 97] += 1
            while freq[ord(s[r]) - 97] >= k:
                res += n - r
                freq[ord(s[l]) - 97] -= 1
                l += 1
        return res
