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

# https://leetcode.com/problems/valid-parentheses/description/
class Solution:

    @timeit
    def isValid(self, s: str) -> bool:
        brackets = {"{" : "}", "[" : "]", "(" : ")"}
        seq = []
        for char in s:
            if char in brackets.keys():
                seq.append(char)
            elif char != brackets[seq.pop()]:
                return False
        return len(seq) == 0

        
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("()[]{}", True),
        ("(]", False),
         ("(()", False),
        ("([])", True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.isValid(input), expected)


    
   