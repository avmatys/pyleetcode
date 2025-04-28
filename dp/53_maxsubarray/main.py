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


# https://leetcode.com/problems/maximum-subarray/description/
class Solution:

    @timeit
    def maxSubArray(self, nums: List[int]) -> int:
        # Store sum of subarray, ending in the position i-th
        nums_count = len(nums)
        dp = [0] * nums_count
        # Set base case
        dp[0] = nums[0]
        for i in range(1, nums_count):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) # We define what is better - add to old subarray or build a new one which is better
        return max(dp)
    

# Another version without dp and without additional memory
# Simple and clear version
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        csum = nums[0]
        for i in range(1,n):
            # Start a new sequence
            if csum < 0:
                csum = nums[i]
            else:
                csum += nums[i]
            res = max(res, csum)
        return res



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ([-2,1,-3,4,-1,2,1,-5,4], 6),
                ([1], 1),
                ([5,4,-1,7,8], 23)
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxSubArray(input), expected)

    
   
