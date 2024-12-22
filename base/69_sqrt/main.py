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


# https://leetcode.com/problems/container-with-most-water/description/
class Solution:

    @timeit
    def mySqrt(self, x):
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if x / mid == mid:
                return mid
            elif x / mid > mid:
                left = mid + 1
            else:
                right = mid - 1
        return right
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (4,2),
        (8,2),
        (100, 10),
        (105,10),
        (110, 10),
        (122, 11),
        (0,0),
        (1,1),
        (2,1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.mySqrt(input), expected)

    
   