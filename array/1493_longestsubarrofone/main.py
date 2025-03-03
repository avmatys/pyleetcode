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


# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
class Solution:

    @timeit
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        k = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,1,1,0,0,0,1,1,1,1,0], 4)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.longestSubarray(input), expected)

    
   