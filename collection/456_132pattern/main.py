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


# https://leetcode.com/problems/132-pattern/description/
class Solution:

    @timeit
    def find132pattern(self, nums: List[int]) -> bool:
        
        # Base check
        n = len(nums)
        if n < 3:
            return False
        
        # Additional array for min elements at each position in the array
        mins = [-1] * n
        mins[0] = nums[0]
        for i in range(1, n):
            mins[i] = min(mins[i-1], nums[i])

        # Check if 132 pattern can be build
        # Start from the end of the nums
        stack = []
        for i in range(n - 1, -1, -1):
            if nums[i] <= mins[i]:
                continue
            # Remove elements, which are smaller than current min
            while stack and stack[-1] <= mins[i]:
                stack.pop()
            if stack and stack[-1] < nums[i]:
                return True
            stack.append(nums[i])
        return False
            

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
             ([1,2,3,4], False),
             ([3,1,4,2], True),
             ([-1,3,2,0], True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.find132pattern(input), expected)

    
   