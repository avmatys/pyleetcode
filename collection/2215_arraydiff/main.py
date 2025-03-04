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


# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
class Solution:

    @timeit
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1-set2),list(set2-set1)]


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
       (([1,2,3], [2,4,6]), [[1,3],[4,6]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findDifference(*input), expected)

    
   