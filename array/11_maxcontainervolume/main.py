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
    def maxArea(self, height: List[int]) -> int:
        
        # Initial value
        max_area = 0

        # Set 2 pointers
        left = 0
        right = len(height) - 1

        # Process while not finished
        while left < right:
            # Calc current volume
            curr_area = min(height[left], height[right]) * (right - left)
            # Check if it's more than prev one
            if curr_area > max_area:
                max_area = curr_area
            # Try to find better left or right
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [([1,8,6,2,5,4,8,3,7], 49),
             ([1,1], 1),
             ([1,2,1], 2),
             ([1,1,1,5,6,1000000000,1000,9,100,78,5], 1000),
             ([1,2,4,3],4)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxArea(input), expected)

    
   