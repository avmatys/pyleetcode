from typing import List
from datetime import datetime
import sys

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/island-perimeter
class Solution:

    @timeit
    def islandPerimeter(self, grid: List[List[int]]) -> int:
       
        row_count = len(grid)
        column_count = len(grid[0])
       
        def count_neighbours(row: int, column:int):
            DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            count = 0
            for offset_i, offset_j in DIRECTIONS:
                i = row + offset_i
                j = column + offset_j
                if i < 0 or i >= row_count or j < 0 or j >= column_count:
                    continue
                if grid[i][j] == 1:
                    count += 1
            return count

        result = 0
        for i in range(row_count):
            for j in range(column_count):
                if grid[i][j] == 1:
                    result += (4 - count_neighbours(i, j))
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]],16),
        ([[1]], 4),
        ([[1,0]], 4)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.islandPerimeter(input), expected)


    
   