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


# https://leetcode.com/problems/minimum-size-subarray-sum/description/
class Solution:

    @timeit
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:  
       
        # Sliding window
        n = len(nums)
        size = n + 1
        start = 0
        end = 0
        sum = 0
        for end in range(n):
            sum += nums[end]
            while sum >= target:
                size = min(size, end - start + 1)
                sum -= nums[start]
                start += 1
                
        return 0 if size == n + 1 else size


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [((7, [2,3,1,2,4,3]), 2),
             ((4, [1,4,4]), 1),
             ((11, [1,1,1,1,1,1,1,1]), 0)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minSubArrayLen(*input), expected)

    
   