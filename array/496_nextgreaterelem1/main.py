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


# https://leetcode.com/problems/next-greater-element-i/description/
class Solution:

    @timeit
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1] < num:
                stack.pop()
            map[num] = stack[-1] if stack else -1
            stack.append(num)
        result = [map[num] for num in nums1]
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
             (([4,1,2], [1,3,4,2]), [-1,3,-1]),
             (([2,4], [1,2,3,4]), [3,-1])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.nextGreaterElement(*input), expected)

    
   