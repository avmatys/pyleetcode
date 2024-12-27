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


# https://leetcode.com/problems/subsets-ii/description/
class Solution:

    @timeit
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
        size = len(sorted_nums)
        def generate_subset(subset, start_idx, k):
            result.append(subset[:])
            for i in range(start_idx, size):
                if i == start_idx or sorted_nums[i-1] != sorted_nums[i]:
                    subset.append(sorted_nums[i])
                    generate_subset(subset, i + 1, k + 1)
                    subset.pop()

        generate_subset([], 0, 0)
        return result
     

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]]),
                ([0], [[],[0]])
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.subsetsWithDup(input), expected)

   
    