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

# https://leetcode.com/problems/ransom-note/
class Solution:

    @timeit
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_chars = [0] * 128
        for char in magazine:
            magazine_chars[ord(char)] += 1
        for char in ransomNote:
            magazine_chars[ord(char)] -= 1
            if magazine_chars[ord(char)] < 0:
                return False
        return True
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("a", "b"), False),
        (("aa", "aab"), True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.canConstruct(*input), expected)


    
   