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

# https://leetcode.com/problems/missing-number/description
class Solution:

    @timeit
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        result = 0
        # x ^ x = 0
        # x ^ 0 = x
        for i in range(n):
            result ^= i
        for num in nums:
            result ^= num
        return result

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([3,0,1]), 2),
        (([9,6,4,2,3,5,7,0,1]), 8)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.missingNumber(input), expected)


    
   