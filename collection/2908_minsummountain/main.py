from typing import List
from datetime import datetime


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/description/
class Solution:

    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        min_right = [nums[-1]] * n
        for i in range(n-2, -1, -1):
            min_right[i] = min(nums[i], min_right[i+1])
        min_left = nums[0]
        min_sum = float('inf')
        for i in range(1, n-1):
            if min_left < nums[i] and nums[i] > min_right[i+1]:
                min_sum = min(min_sum, min_left + nums[i] + min_right[i+1])
            min_left = min(min_left, nums[i])
        return -1 if min_sum == float('inf') else min_sum


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([5,4,8,7,10,2], 13)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minimumSum(input), expected)

    
   
