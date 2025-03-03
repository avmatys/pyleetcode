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


# https://leetcode.com/problems/find-pivot-index 
class Solution:

    @timeit
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_left = [0] * n
        for i in range(1, n):  
            prefix_left[i] = prefix_left[i-1] + nums[i-1]
        prefix_right = [0] * n
        for i in range(n-2, -1, -1):
            prefix_right[i] = prefix_right[i+1] + nums[i+1]
        for i in range(n):
            if prefix_left[i] == prefix_right[i]:
                return i
        return -1

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([-5,1,5,0,-7], -1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.pivotIndex(input), expected)

    
   