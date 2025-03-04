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


# https://leetcode.com/problems/4sum/description/
class Solution:

    @timeit
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Sort initial array
        nums.sort()

        # Select each element as a fixed one 
        # Use 2 pointer approach to check sum of the 2 elements 
        quadruplets = []
        for first_fixed_idx in range(len(nums) - 3):
            # Skip the same ids
            if first_fixed_idx > 0 and nums[first_fixed_idx] == nums[first_fixed_idx-1]:
                continue
            for second_fixed_idx in range(first_fixed_idx + 1, len(nums)-2):
                # Skip the same ids
                if second_fixed_idx > first_fixed_idx + 1 and nums[second_fixed_idx] == nums[second_fixed_idx-1]:
                     continue
                # Set 2 pointers and work with them
                needed_sum = target - nums[first_fixed_idx] - nums[second_fixed_idx]
                left_idx = second_fixed_idx + 1
                right_idx = len(nums) - 1
                while left_idx < right_idx:
                    current_sum = nums[left_idx] + nums[right_idx]
                    if current_sum == needed_sum:
                        print(f"First {first_fixed_idx} Second {second_fixed_idx} Left {left_idx} Right {right_idx}")
                        quadruplets.append([nums[first_fixed_idx], nums[second_fixed_idx], nums[left_idx], nums[right_idx]])
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
                    
        return quadruplets


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,0,-1,0,-2,2], 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
        (([2,2,2,2,2], 8), [[2,2,2,2]]),
        (([-2,-1,-1,1,1,2,2], 0), [[-2,-1,1,2],[-1,-1,1,1]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.fourSum(input[0], input[1]), expected)

    
   