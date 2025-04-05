from typing import List
from datetime import datetime
from typing import Optional
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
class Solution:
   
    def permutate(self, nums, idx, xor_sum):
        if idx == len(nums):
            return xor_sum
        with_sum = self.permutate(nums, idx+1, xor_sum ^ nums[idx])
        without_sum = self.permutate(nums, idx+1, xor_sum)
        return with_sum + without_sum

    def subsetXORSum(self, nums: List[int]) -> int:
        return self.permutate(nums, 0, 0)

