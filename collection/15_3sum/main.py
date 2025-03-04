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


# https://leetcode.com/problems/3sum/description/
class Solution:

    @timeit
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort initial array
        nums.sort()

        # Select each element as a fixed one 
        # Use 2 pointer approach to check sum of the 2 elements 
        triplets = []
        for fixed_idx in range(len(nums) - 2):
            # Skip the same ids
            if fixed_idx > 0 and nums[fixed_idx] == nums[fixed_idx-1]:
                continue

            # Set 2 pointers and work with them
            needed_sum = 0 - nums[fixed_idx]
            left_idx = fixed_idx + 1
            right_idx = len(nums) - 1
            while left_idx < right_idx:
                current_sum = nums[left_idx] + nums[right_idx]
                if current_sum == needed_sum:
                    triplets.append([nums[fixed_idx], nums[left_idx], nums[right_idx]])
                    # Move both pointers to the next not equal element
                    left_idx += 1
                    right_idx -= 1
                    # Check if move to one element is enough
                    # Array has elements with the same value
                    while left_idx < right_idx and nums[left_idx] == nums[left_idx-1]:
                        left_idx += 1
                    while left_idx < right_idx and nums[right_idx] == nums[right_idx+1]:
                        right_idx -= 1
                # As our arry is sorted ascending and sum is more that needed, we should decrease it
                # We can decrease it by moving right pointer on 1 elem left
                elif current_sum > needed_sum:
                    right_idx -= 1
                # Sum is smaller than needed
                # We should add left elem index
                else:
                    left_idx += 1
                    
        return triplets


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0],[[0,0,0]]),
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.threeSum(input), expected)

    
   