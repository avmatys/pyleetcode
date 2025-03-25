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


# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/
class Solution:
    def count_gaps(self, rectangles, axis): 
        intervals = sorted(rectangles, key = lambda r: r[axis]) # x=0, y=1 
        curr_end, gap_cnt = intervals[0][axis + 2], 0
        for i in range(1, len(intervals)):
            if intervals[i][axis] >= curr_end:
                gap_cnt += 1
            curr_end = max(curr_end, intervals[i][axis + 2])
        return gap_cnt

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return self.count_gaps(rectangles, 0) >= 2 or self.count_gaps(rectangles, 1) >= 2


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]), True),
        ((4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]), False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.checkValidCuts(*input), expected)

    
   
