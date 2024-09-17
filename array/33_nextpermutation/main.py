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


# https://leetcode.com/problems/next-permutation/description
class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        # Handle simple base case
        if n <= 1:
            return nums
      
        # Find position, when element changes from big to small
        i = n - 1
        start_idx = -1
        while i > 0:
            i -= 1
            if nums[i] < nums[i + 1]: 
                start_idx = i
                break
        
        # Base case - we found an index
        if start_idx >= 0:
            # Find index of element, which is min in subarray[start_idx:] and greater than nums[start_idx]
            min_idx = start_idx + 1
            i = min_idx
            while i < n:
                if nums[i] > nums[start_idx] and nums[i] < nums[min_idx]:
                    min_idx = i
                i += 1
            # We are ready to swap elements and sort subarray
            if min_idx > start_idx and min_idx < n:
                nums[start_idx], nums[min_idx] = nums[min_idx], nums[start_idx]
                nums[start_idx + 1:] = sorted(nums[start_idx + 1:])
     
        # Corner case - array is sorted descending
        else:
            nums[:] = sorted(nums[:])

        return nums




def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,3], [3,1]),
        ([3,1], [1,3]),
        ([1,2,3], [1,3,2]),
        ([1,1,5], [1,5,1]),
        ([1,5,1], [5,1,1]),
        ([4,3,2,5,4,3,1], [4,3,3,1,2,4,5]),
        ([3,2,1], [1,2,3])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.nextPermutation(input), expected)

    
   