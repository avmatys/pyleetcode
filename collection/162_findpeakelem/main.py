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


# https://leetcode.com/problems/find-peak-element/
class Solution:

    @timeit
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1   
        return left


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3,1], 2),
        ([1,2,1,3,5,6,4], 5),
        ([20,2,1,3,5,6,7], 6),
        ([1,2,1,3,5,6,40], 6),
        ([1,2], 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findPeakElement(input), expected)

    
   
