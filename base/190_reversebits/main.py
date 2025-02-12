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


# https://leetcode.com/problems/reverse-bits/description/
class Solution:

    @timeit
    def reverseBits(self, n: int) -> int: 
        rev = 0b0
        for _ in range(32):
            bit = n & 1
            rev = rev << 1
            rev = rev | bit
            n = n >> 1
        return rev

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (0b00000010100101000001111010011100, 0b00111001011110000010100101000000)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.reverseBits(input), expected)

    
   