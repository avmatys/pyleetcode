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


# https://leetcode.com/problems/search-in-rotated-sorted-array/description
class Solution:

    def search(self, nums: List[int], target: int) -> int:

        left = 0 
        right = len(nums) - 1
        result = -1

        while left <= right:
            # Get middle element
            mid = (left + right) // 2
            # Probably it's what we need
            if nums[mid] == target:
                result = mid
                break
            # If no - we shoud identify area in which we should continue search
            if nums[left] <= nums[mid]:
                # This means that [left:mid] is sorted ascending
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # This means that [mid:right] is probablu sorted ascending
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
    
        return result



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([4,5,6,7,0,1,2], 4), 0),
        (([4,5,6,7,0,1,2], 0), 4),
        (([1], 2), -1),
        (([3,1], 1), 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.search(*input), expected)

    
   