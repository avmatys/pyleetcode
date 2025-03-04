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


# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:

    @timeit
    def removeDuplicates(self, nums: List[int]) -> int:
       
        unique_idx = 0
        duplicate_idx = 1
        
        while duplicate_idx < len(nums):
            # If it's not a duplicate - move non duplicate in the beginning
            if nums[unique_idx] != nums[duplicate_idx]:
                unique_idx += 1
                nums[unique_idx] = nums[duplicate_idx]
            # Iterate through array
            duplicate_idx += 1
                          
        # Size is idx + 1
        return unique_idx + 1      


def judge(nums, expected_nums, size, expected_size):
    assert size == expected_size
    for i in range(size):
        assert nums[i] == expected_nums[i]


    
if __name__ == '__main__':
    solution = Solution()
    # Case 1
    nums = [1,1,1,1,1,1,2,2,3,4,5,5,5,7,8,8]
    expected_nums = [1,2,3,4,5,7,8]
    arr_size = solution.removeDuplicates(nums)
    judge(nums, expected_nums, arr_size, len(expected_nums))
    # Case 2
    nums = [0,0,1,1,1,2,2,3,3,4]
    expected_nums = [0,1,2,3,4]
    arr_size = solution.removeDuplicates(nums)
    judge(nums, expected_nums, arr_size, len(expected_nums))
    # Case 3
    nums = [0,0]
    expected_nums = [0]
    arr_size = solution.removeDuplicates(nums)
    judge(nums, expected_nums, arr_size, len(expected_nums))
    # Case 4
    nums = [-2,-2,-2,-1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
    expected_nums = [-2,-1,0,1]
    arr_size = solution.removeDuplicates(nums)
    judge(nums, expected_nums, arr_size, len(expected_nums))

    
   