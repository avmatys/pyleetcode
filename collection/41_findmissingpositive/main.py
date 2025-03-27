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


# https://leetcode.com/problems/first-missing-positive/description/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n, i = len(nums), 0
        while i < n:
            idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[idx]:
                nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3,4,-1,1], 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.firstMissingPositive(input), expected)


    
   
