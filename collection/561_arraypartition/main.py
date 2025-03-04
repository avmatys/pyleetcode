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


# https://leetcode.com/problems/array-partition/description
class Solution:

    @timeit
    def arrayPairSum(self, nums: List[int]) -> int:
        sorter_nums = sorted(nums)
        sum = 0
        for idx in range(0, len(sorter_nums), 2):
            sum += sorter_nums[idx]
        return sum
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,4,3,2]), 4),
        (([6,2,6,5,1,2]), 9)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.arrayPairSum(input), expected)


    
   