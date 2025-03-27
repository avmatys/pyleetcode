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


# https://leetcode.com/problems/maximum-strength-of-a-group/description/
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        min_res = max_res = nums[0]
        for num in nums[1:]:
            tmp_min, tmp_max = min_res * num, max_res * num
            min_res = min(min_res, tmp_min, tmp_max, num)
            max_res = max(max_res, tmp_min, tmp_max, num)
        return max_res

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3,-1,-5,2,5,-9], 1350)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxStrength(input), expected)
