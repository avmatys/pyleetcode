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

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution:

    @timeit
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        shots = len(points)
        if shots < 2:
            return shots
        sorted_points = sorted(points, key=lambda coord:coord[1])
        curr_end = sorted_points[0][1]
        for coord in sorted_points[1:]:
            if curr_end >= coord[0]:
                shots -= 1
            else:
                curr_end = coord[1]
        return shots

class SolutionRev:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        spoints = sorted(points, key=lambda x: x[1])
        count = len(spoints)
        last = 0
        for i in range(1, len(spoints)):
            if spoints[last][1] >= spoints[i][0]:
                count -= 1
            else:
                last = i
        return count      

    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[10,16],[2,8],[1,6],[7,12]], 2),
        ([[1,2],[3,4],[5,6],[7,8]], 4),
        ([[1,100],[2,101],[3,102],[4,103]], 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findMinArrowShots(input), expected)


    
   
