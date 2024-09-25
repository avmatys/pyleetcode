from typing import List
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


# https://leetcode.com/problems/permutations/
class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = []
        # Sort input data in order to generate unique permutation
        nums.sort()

        def generate(nums: List[int], path: List[int]):
            n = len(nums)
            if n == 0:
                result.append(path[:])
                return
            else:
                for i in range(n):
                    if i > 0 and nums[i-1] == nums[i]:
                        # Skip case in order to avoid duplicates
                        continue
                    next_nums = nums[:i] + nums[i+1:]
                    next_path = path + [nums[i]] # New array, backtracking is not needed
                    generate(next_nums, next_path)

        generate(nums, [])
        return result
  


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([1,1,2],[[1,1,2],[1,2,1], [2,1,1]]),
        ([1], [[1]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.permuteUnique(input), expected)

    
   