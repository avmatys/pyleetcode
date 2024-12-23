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


# https://leetcode.com/problems/combination-sum-iii/description/
class Solution:

    @timeit
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sorted_candidates = sorted(candidates)
        size = len(sorted_candidates)
        def combine(nums, curr_target, idx):
            if curr_target > target:
                return
            if curr_target == target:
                result.append(nums[:])
                return
            for i in range(idx, size):
                nums.append(sorted_candidates[i])
                combine(nums, curr_target + sorted_candidates[i], i)
                nums.pop()
        combine([], 0, 0)
        return result
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([2,3,6,7],7),[[2,2,3],[7]]),
        (([2,3,5],8),[[2,2,2,2],[2,3,3],[3,5]]),
        (([2],1), [])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.combinationSum(*input), expected)

    
   