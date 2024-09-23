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


# https://leetcode.com/problems/combination-sum-ii//
class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()
    
        def dfs(current: List[int], sum: int, idx: int):
            if sum == target:
                result.append(current[:])
                return
            else:
                for i in range(idx, len(candidates)):
                    # Additional check to avoid usage of the same element
                    if i > idx and candidates[i] == candidates[i - 1]:
                        continue
                    next_sum = sum + candidates[i]
                    if next_sum > target:
                        break
                    current.append(candidates[i])
                    # Go to the next element
                    dfs(current, next_sum, i + 1)
                    current.pop()
        
        dfs([], 0, 0)
        return result
        


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([10,1,2,7,6,1,5], 8), [[1,1,6],[1,2,5],[1,7],[2,6]]),
        (([2,5,2,1,2], 5),[[1,2,2],[5]]),
        (([2], 1), [])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.combinationSum2(*input), expected)

    
   