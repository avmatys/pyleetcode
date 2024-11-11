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


# https://leetcode.com/problems/rotate-array/description/
class Solution:

    @timeit
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start: int, end:int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        rotate_idx = k % n
        reverse(0, n - 1)
        reverse(0, rotate_idx - 1)
        reverse(rotate_idx, n - 1)

            



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([-1,-100,3,99], 2), [3,99,-1,-100]),
        (([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])  
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        solution.rotate(*input)
        judge(input[0], expected)


    
   