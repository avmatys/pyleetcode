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


# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        # First iteration from the start without additional vars for prefix product
        for i in range(1, n):
            output[i] = nums[i - 1] * output[i - 1]
        # Second iteration from the end with additional var to store temp suffix product
        tmp = 1
        for i in range(n - 2, -1, -1):
            tmp *= nums[i + 1]
            output[i] *= tmp
        return output




def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.productExceptSelf(input), expected)

    
   