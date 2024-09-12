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

# https://leetcode.com/problems/intersection-of-two-arrays
class Solution:

    @timeit
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:     

        # Implement recursive quick sort
        def sort(nums: List[int]):
            
            less = []
            equal = []
            greater = []

            if len(nums) > 1:
                pivot = nums[0]
                for num in nums:
                    if num < pivot:
                        less.append(num)
                    if num == pivot:
                        equal.append(num)
                    elif num > pivot:
                        greater.append(num)
                return sort(less) + equal + sort(greater)
            else:
                return nums
            
        # Sort input arrays
        sorted_nums1 = sort(nums1)
        sorted_nums2 = sort(nums2)

        # Set pointers for each array and iterate through arrays to find intersected elements
        nums1_idx = 0
        nums2_idx = 0

        #Intersect
        result = []
        while nums1_idx < len(sorted_nums1) and nums2_idx < len(sorted_nums2):
            if sorted_nums1[nums1_idx] == sorted_nums2[nums2_idx]:
                if nums1_idx > 0:
                    if sorted_nums1[nums1_idx] == sorted_nums1[nums1_idx-1]:
                        nums1_idx += 1
                        nums2_idx += 1
                        continue
                result.append(sorted_nums1[nums1_idx])
                nums1_idx += 1
                nums2_idx += 1
            elif sorted_nums1[nums1_idx] < sorted_nums2[nums2_idx]:
                nums1_idx += 1
            else:
                nums2_idx += 1
    
        return result
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([2,2],[2]),[2]),
        (([0,1,2,4,5,7], [0,7,4,1]), [0,1,4,7]),
        (([4,9,5], [9,4,9,8,4]), [4,9])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.intersection(*input), expected)


    
   