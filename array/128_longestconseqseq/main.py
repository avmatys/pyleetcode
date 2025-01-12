from typing import List
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:

    @timeit
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        if len(unique_nums) < 2:
            return len(unique_nums)
        starts = []
        for num in unique_nums:
            if num - 1 not in unique_nums:
                starts.append(num)
        max_len = 1
        for start_num in starts:
            curr_len = 1
            while start_num + curr_len in unique_nums:
                curr_len += 1
            max_len = max(max_len, curr_len)
        return max_len
        
    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([1,2,0,1], 3),
        ([0], 1),
        ([0,0], 1),
        ([], 0),
        ([9,1,4,7,3,-1,0,5,8,-1,6], 7)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.longestConsecutive(input), expected)


    
   