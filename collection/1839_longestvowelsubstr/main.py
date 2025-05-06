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

# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        n = len(word)
        i = 0
        while i < n:
            # Check start of the new sequence
            if word[i] == 'a':
                j = i + 1
                unique = 0
                while j < n and word[j-1] <= word[j]:
                    unique += word[j-1] < word[j]
                    j += 1
                if unique == 4:
                    res = max(res, j - i)
                i = j
            else:
                i += 1
        return res
