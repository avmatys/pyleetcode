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
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def combine(nums, start_num, curr_k, curr_n):
            if curr_k > k or curr_n > n:
                return
            if curr_k == k and curr_n == n:
                result.append(nums[:])
                return
            for i in range(start_num, 10):
                nums.append(i)
                combine(nums, i + 1, curr_k + 1, curr_n + i)
                nums.pop()
        
        combine([], 1, 0, 0)
        return result
           
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((3,7),[[1,2,4]]),
        ((3,9),[[1,2,6],[1,3,5],[2,3,4]]),
        ((4,1), [])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.combinationSum3(*input), expected)

    
   