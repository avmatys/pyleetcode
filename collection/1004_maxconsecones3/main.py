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


# https://leetcode.com/problems/max-consecutive-ones-iii/description/
class Solution:

    @timeit
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,1,1,0,0,0,1,1,1,1,0], 2), 6)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.longestOnes(*input), expected)

    
   