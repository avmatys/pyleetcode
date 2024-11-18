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


# https://leetcode.com/problems/house-robber-ii/description/
class Solution:

    @timeit
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 4:
            return max(nums)
        
        first_sum = [0] * (n - 1) # Include first element to the sum
        first_sum[0] = nums[0]
        first_sum[1] = max(nums[0], nums[1])

        last_sum = [0] * (n -1) # Include last element to the sum
        last_sum[0] = nums[1]
        last_sum[1] = max(nums[1], nums[2])

        for i in range(2, n - 1):
            first_sum[i] = max(nums[i] + first_sum[i - 2], first_sum[i - 1]) 
            last_sum[i] = max(nums[i + 1] + last_sum[i - 2], last_sum[i - 1]) 
    
        return max(first_sum[n - 2], last_sum[n - 2])
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
             ([2,3,2], 3),
             ([1,2,3,1], 4),
             ([1,2,3], 3),
             ([2,7,9,3,1], 11),
             ([2,1,1,2], 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.rob(input), expected)

    
   