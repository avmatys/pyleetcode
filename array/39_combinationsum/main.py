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


# https://leetcode.com/problems/combination-sum/description/
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        
        result = []
        def dfs(current: List[int], sum: int, idx: int):
            print(f"{current} sum {sum}")
            if sum == target:
                result.append(current[:])
                return
            else:
                for i in range(idx, len(candidates)):
                    next_sum = sum + candidates[i]
                    if next_sum > target:
                        break
                    current.append(candidates[i])
                    dfs(current, next_sum, i)
                    current.pop()

        dfs([], 0, 0)
        return result




def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([2,3,6,7], 7), [[2,2,3],[7]]),
        (([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]]),
        (([2], 1), [])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.combinationSum(*input), expected)

    
   