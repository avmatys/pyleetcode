from typing import List
from datetime import datetime
import sys

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
class Solution:

    @timeit
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      
        n = len(nums)
        for i in range(n):
            if nums[i] == i + 1:
                continue
            move_idx = nums[i] - 1
            while nums[move_idx] != move_idx + 1:
                next_idx = nums[move_idx] - 1
                nums[move_idx] = move_idx + 1
                move_idx = next_idx

        result = []
        for i in range(n):
            if nums[i] != i + 1:
                result.append(i + 1)

        return result      


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([4,3,2,7,8,2,3,1],[5,6]),
        ([1,1], [2]),
        ([4,3,2,7,7,2,3,1],[5,6,8])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findDisappearedNumbers(input), expected)


    
   