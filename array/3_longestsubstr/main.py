from typing import List
from datetime import datetime
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

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:

    @timeit
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        left = 0
        right = 1
        max_len = 1
        symbols = [False] * 128
        symbols[ord(s[left])] = True
        while left < n and right < n:
            right_code = ord(s[right])
            if not symbols[right_code]:
                symbols[right_code] = True
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                while symbols[right_code]:
                    symbols[ord(s[left])] = False
                    left += 1
        return max_len
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        (" ", 1),
        ("dvdf", 3),
        ("ckilbkd", 5),
        ("tmmzuxt", 5)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.lengthOfLongestSubstring(input), expected)


    
   