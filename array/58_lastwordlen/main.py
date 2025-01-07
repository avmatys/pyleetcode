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

# https://leetcode.com/problems/length-of-last-word/
class Solution:

    @timeit
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ' ':
                if result > 0:
                    break
                else:
                    continue
            result += 1
        return result
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.lengthOfLastWord(input), expected)


    
   