from typing import List
from datetime import datetime
import heapq


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/sort-colors
class Solution:

    @timeit
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # DNF algorithm
        mid = 1

        left = 0
        right = len(nums) - 1
        curr = 0

        while curr <= right:
            print(f"nums: {nums} curr {curr} left {left} right {right}")
            if nums[curr] < mid:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] > mid:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1

        return nums


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([2,0,2,1,1,0]), [0,0,1,1,2,2]),
        (([2,0,2,0,1,1]), [0,0,1,1,2,2]),
        (([2,2,1,0,0,2,1,1,0,0]), [0,0,0,0,1,1,1,2,2,2]),
        (([2,0,1]), [0,1,2])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.sortColors(input), expected)


    
   