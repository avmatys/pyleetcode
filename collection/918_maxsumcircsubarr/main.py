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


# https://leetcode.com/problems/maximum-sum-circular-subarray/
class Solution:

    @timeit
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        curr_max = max_sum = nums[0]
        curr_min = min_sum = nums[0]
        total = nums[0]
        for i in range(1, n):
            curr_max = max(curr_max + nums[i], nums[i])
            max_sum = max(max_sum, curr_max)
            curr_min = min(curr_min + nums[i], nums[i])
            min_sum = min(min_sum, curr_min)
            total += nums[i]
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,-2,3,-2], 3),
        ([1,2,5,-4,10,20], 38)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxSubarraySumCircular(input), expected)

    
   