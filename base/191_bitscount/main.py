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


# https://leetcode.com/problems/number-of-1-bits/description/
class Solution:

    @timeit
    def hammingWeight(self, n: int) -> int:
        return 0 if n == 0 else (n & 1) + self.hammingWeight(n >> 1)

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (21, 3),
        (128, 1),
        (11, 3),
        (2147483645, 30)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.hammingWeight(input), expected)

    
   