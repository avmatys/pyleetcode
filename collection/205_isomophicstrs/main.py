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

# https://leetcode.com/problems/isomorphic-strings/description/
class Solution:

    @timeit
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] = i
            if t[i] not in map_t:
                map_t[t[i]] = i
            if map_s[s[i]] != map_t[t[i]]:
                return False
        return True
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("egg", "add"), True),
        (("badc", "baba"), False),
        (("paper", "title"), True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.isIsomorphic(*input), expected)


    
   