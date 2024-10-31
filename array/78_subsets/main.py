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


# https://leetcode.com/problems/sort-colors
class Solution:

    @timeit
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        result = []

        def build_subset(array: List[int], first: int):
            result.append(array[:])
            for i in range(first, n):
                array.append(nums[i])
                build_subset(array, i + 1)
                array.pop()
            
        build_subset([], 0)
        
        return result



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    for arr in result:
        assert arr in  expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
        (([0]), [[],[0]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.subsets(input), expected)


    
   