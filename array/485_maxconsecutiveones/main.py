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


# https://leetcode.com/problems/max-consecutive-ones/description
class Solution:

    @timeit
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_cnt = 0
        max_cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                cur_cnt += 1
            if nums[i] == 0 or i == n - 1:
                max_cnt = max(cur_cnt, max_cnt)
                cur_cnt = 0
        return max_cnt



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,1,0,1,1,1], 3),
        ([1,0,1,1,0,1], 2),
        ([1,1,1,1,1,1], 6),
        ([0,0,0,0,0,0], 0)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findMaxConsecutiveOnes(input), expected)


    
   