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


# https://leetcode.com/problems/move-zeroes/description
class Solution:


    @timeit
    def moveZeroes(self, nums: List[int]) -> None:               
        
        n = len(nums)
        left = 0
  
        for i in range(n):
            # Check if value is non-zero
            if nums[i] != 0:
                # If our pointer of the correct array is not equal to the current - copy
                if left != i:
                    nums[left] = nums[i]
                # Move to the next element
                left += 1
        
        # Just set zeros to the least elements
        for i in range(left, n):
            nums[i] = 0
    
        return nums
    
    
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([0],[0]),
        ([1],[1]),
        ([0,1,0,3,12], [1,3,12,0,0]),
        ([0,1,2,0,3,4,0,0,6,8,9,0], [1,2,3,4,6,8,9,0,0,0,0,0])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.moveZeroes(input), expected)


    
   