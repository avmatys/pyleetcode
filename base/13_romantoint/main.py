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

# https://leetcode.com/problems/roman-to-integer/description/
class Solution:
    def romanToInt(self, s: str) -> int:
        smap = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
        last  = 0
        result = 0
        for i in range(len(s) - 1, -1, -1):
            if smap[s[i]] >= last:
                result += smap[s[i]]
            else:
                result -= smap[s[i]]
            last = smap[s[i]]
        return result

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("III", 3),
        ("LVIII", 58)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.romanToInt(input), expected)

