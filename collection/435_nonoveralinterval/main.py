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

# https://leetcode.com/problems/non-overlapping-intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sintvls = sorted(intervals, key = lambda pair: pair[1])
        last, count = 0, 0
        for i in range(1, len(sintvls)):
            # Intersection
            if sintvls[last][1] > sintvls[i][0]:
                count += 1
            else:
                last = i
        return count

    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[1,2],[2,3],[3,4],[1,3]], 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.eraseOverlapIntervals(input), expected)


    
   
