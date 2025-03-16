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


# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c
class Solution:

    @timeit
    def minFlips(self, a: int, b: int, c: int) -> int:
        counter = 0
        while a > 0 or b > 0 or c > 0:
            if (c & 1) != ((a & 1) | (b & 1)):
                if c & 1:
                    counter += c & 1
                else:
                    counter += a & 1
                    counter += b & 1
            a, b, c = a >> 1, b >> 1, c >> 1
        return counter

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((2,6,5), 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minFlips(*input), expected)

    
   
