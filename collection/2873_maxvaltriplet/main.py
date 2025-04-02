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


# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/
class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triplet = 0
        max_val = nums[0]
        max_diff = 0
        for i in range(1, len(nums)):
            max_triplet = max(max_triplet, max_diff * nums[i])
            max_diff = max(max_diff, max_val - nums[i])
            max_val = max(max_val, nums[i])
        return max_triplet


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,10,3,4,19], 133)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maximumTripletValue(input), expected)

    
   
