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


# https://leetcode.com/problems/bitwise-and-of-numbers-range/description 
class Solution:

    @timeit
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            cnt += 1
        return left << cnt


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((5,7), 4),
        ((5,13), 0),
        ((3,3), 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.rangeBitwiseAnd(*input), expected)

    
   