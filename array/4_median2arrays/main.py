
from typing import List
from datetime import datetime
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

# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:

    @timeit
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m:
            n, m = m, n
            nums1, nums2 = nums2, nums1
        partition_total = (n + m + 1) // 2
        left, right = 0, n
        while left <= right:
            partition_x = (left + right) // 2
            partition_y = partition_total - partition_x
            min_x = float('-inf') if partition_x == 0 else nums1[partition_x-1]
            max_x = float('inf') if partition_x == n else nums1[partition_x]
            min_y = float('-inf') if partition_y == 0 else nums2[partition_y-1]
            max_y = float('inf') if partition_y == m else nums2[partition_y]
            if min_x <= max_y and min_y <= max_x:
                if (n + m) % 2 == 0:
                    return (max(min_x, min_y) + min(max_x, max_y)) / 2
                return max(min_x, min_y)
            elif max_x > min_y:
                right = partition_x - 1
            else:
                left = partition_x + 1
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    
if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([2], []), 2),
        (([1,2], [1]), 1.),
        (([1,2,3], [2]), 2.),
        (([1,2,3], [1]), 1.5)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findMedianSortedArrays(*input), expected)


    
   