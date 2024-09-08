from typing import List
from typing import Optional
from datetime import datetime
from collections import deque

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper



# https://leetcode.com/problems/merge-sorted-array/description
class Solution:

    @timeit
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # Merge 2 arrays - start from the tail
        first_idx = m - 1
        second_idx = n - 1
        current_idx = len(nums1) - 1

        while second_idx >= 0:
            if first_idx >= 0 and nums1[first_idx] > nums2[second_idx]:
                nums1[current_idx] = nums1[first_idx]
                first_idx -= 1
            else:
                nums1[current_idx] = nums2[second_idx]
                second_idx -= 1
            current_idx -= 1

        return nums1
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6]),
        (([1], 1, [], 0), [1]),
        (([0], 0, [1], 1),[1]),
        (([2,0], 1, [1], 1), [1,2])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.merge(input[0], input[1], input[2], input[3]), expected)

    
   