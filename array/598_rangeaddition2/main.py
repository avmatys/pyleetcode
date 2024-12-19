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


# https://leetcode.com/problems/range-addition-ii/description/
class Solution:

    @timeit
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
       if len(ops) == 0:
           return m * n
       min_col = min(ops, key = lambda t: t[0])[0]
       min_rows = min(ops, key = lambda t: t[1])[1]
       return min_col * min_rows

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ((3,3,[[2,2],[3,3]]), 4),
                ((3,3,[[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]), 4),
                ((3,3,[]), 9)               
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxCount(*input), expected)

   
    