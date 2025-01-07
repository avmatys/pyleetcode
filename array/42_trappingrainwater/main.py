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

# https://leetcode.com/problems/candy/description/
class Solution:

    @timeit
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_height = [height[0]] * n
        right_height = [height[-1]] * n
        water = [0] * n
        for i in range(1, n):
            left_height[i] = max(left_height[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            right_height[i] = max(right_height[i + 1], height[i])
        for i in range(n):
            water[i] = min(left_height[i], right_height[i]) - height[i]
        return sum(water)
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([1,0,2,1,0,1,3,2,1,1,2,1,4], 13),
        ([4,2,0,3,2,5], 9)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.trap(input), expected)


    
   