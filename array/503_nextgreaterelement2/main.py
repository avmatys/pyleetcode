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


# https://leetcode.com/problems/next-greater-element-ii/
class Solution:

    @timeit
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = [] # Store in the stack index instead of value
        for i in range(2*n - 1, -1, -1):
            cmp_i = i % n
            while stack and nums[cmp_i] >= nums[stack[-1]]:
                stack.pop()
            result[cmp_i] = nums[stack[-1]] if stack else -1
            stack.append(cmp_i)
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
             ([1,2,1], [2,-1,2]),
             ([1,2,3,4,3], [2,3,4,-1,4])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.nextGreaterElements(input), expected)

    
   