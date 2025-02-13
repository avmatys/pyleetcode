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


# https://leetcode.com/problems/hamming-distance/description/
class Solution:

    @timeit
    def hammingDistance(self, x: int, y: int) -> int:
        return (x^y).bit_count()

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((1, 4), 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.hammingDistance(*input), expected)

    
   