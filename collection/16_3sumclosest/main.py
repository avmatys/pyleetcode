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

# https://leetcode.com/problems/3sum-closest/description/
class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest_sum = float('inf')
        closest_diff = float('inf')
        nums.sort()
        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    return target
                elif curr_sum > target:
                    right -= 1
                else:
                    left += 1
                curr_diff = abs(curr_sum - target) 
                if curr_diff < closest_diff:
                    closest_diff = curr_diff
                    closest_sum = curr_sum
        return closest_sum
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([-1,2,1,-4], 1), 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.threeSumClosest(*input), expected)

    
   
