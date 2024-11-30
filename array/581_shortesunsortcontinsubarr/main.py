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


# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
class Solution:

    @timeit
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)

        # Find idxes where sequence is changed
        left = 0
        right = n - 1
        while left < n - 1 and nums[left + 1] >= nums[left]:
            left += 1        
        while right > 1 and nums[right] >= nums[right - 1]:
            right -= 1

        # Elements are in the correct order
        if left == n - 1:
            return 0

        # Find max and min elemens in the sequence
        min_idx = left
        max_idx = right
        for i in range(left, right + 1):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
        
        # Check elems in the left and right parts of the array
        # And check if they are smaller than all elements
        result_left = left
        result_right = right
        for i in range(left):
            if nums[i] > nums[min_idx]:
                result_left = i
                break
        for i in range(n - 1, right, -1):
            if nums[i] < nums[max_idx]:
                result_right = i
                break
        
        return result_right - result_left + 1

    
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        
        n = len(nums)
        left = -1
        
        # Find right index - from start to end        
        right = -1
        prev_elem = nums[0]
        for i in range(1, n):
            if nums[i] < prev_elem:
                right = i
            else:
                prev_elem = nums[i]

        # Find left index - from end to start
        left = 0
        next_elem = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if next_elem < nums[i]:
                left = i
            else:
                next_elem = nums[i]
        
        return right - left + 1


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ([1,3,2,3,3], 2),
                ([1,2,4,5,3], 3),
                ([1,2,3,3,3], 0),
                ([1,3,2,2,2], 4),
                ([2,6,4,8,10,9,15], 5),
                ([1,2,3,4], 0),
                ([1], 0),
                ([1,3,0,1000,100,5,6,7], 8)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findUnsortedSubarray2(input), expected)

    
   