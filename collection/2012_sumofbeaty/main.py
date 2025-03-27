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


# https://leetcode.com/problems/sum-of-beauty-in-the-array/description/
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        right_min = [nums[-1]] * n
        for i in range(n-2,-1,-1):
            right_min[i] = min(right_min[i+1], nums[i])
        curr_max = nums[0]
        result = 0
        for i in range(1, n-1):
            if curr_max < nums[i] < right_min[i+1]:
                result += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                result += 1
            curr_max = max(curr_max, nums[i])
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([2,4,6,4], 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.sumOfBeauties(input), expected)

    
   
