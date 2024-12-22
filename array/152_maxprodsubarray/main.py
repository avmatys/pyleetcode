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


# https://leetcode.com/problems/maximum-product-subarray/
class Solution:

    @timeit
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curr_min = result
        curr_max = result
        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)
            result = max(result, curr_max)
        return result

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ([-2,3,-4], 24),
                ([2,3,-2,4], 6),
                ([-2,0,-1], 0),
                ([-10,10,10,-10], 10000),
                ([-10,10,-10,0,10,10,-10,-10], 10000)
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxProduct(input), expected)

   
    