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


# https://leetcode.com/problems/regions-cut-by-slashes/?envType=daily-question&envId=2024-08-09
class Solution:

     # Flood fill algorithm to mark all cells in a region
    def _flood_fill(self, ext_grid, row, col):

        grid_size = len(ext_grid)

        # Directions: right, left, down, up
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        # Mark as visited
        queue = [(row, col)]
        ext_grid[row][col] = 1 

        while queue:
            current_cell = queue.pop(0)
            # Check all four directions from the current cell
            for direction in DIRECTIONS:
                next_row = current_cell[0] + direction[0]
                next_col = current_cell[1] + direction[1]
                # If the new cell is valid and unvisited, mark it and add to queue
                if 0 <= next_row < grid_size and 0 <= next_col < grid_size and ext_grid[next_row][next_col] == 0:
                    ext_grid[next_row][next_col] = 1
                    queue.append((next_row, next_col))

    
    @timeit
    def regionsBySlashes(self, grid: List[str]) -> int:

        # Transform input grid to 3x3 matrix for each cell
        grid_size = len(grid)   
        ext_grid = [[0] * (3 * grid_size) for _ in range (3 * grid_size)]

        # Transfor symbols to array from 0 and 1
        for i in range(grid_size):
            for j in range(grid_size):
                ext_grid_i = 3 * i
                ext_grid_j = 3 * j
                # Make
                # 1 0 0
                # 0 1 0
                # 0 0 1
                if grid[i][j] == "\\":
                    ext_grid[ext_grid_i][ext_grid_j] = 1
                    ext_grid[ext_grid_i + 1][ext_grid_j + 1] = 1 
                    ext_grid[ext_grid_i + 2][ext_grid_j + 2] = 1
                # Make 
                # Make
                # 0 0 1
                # 0 1 0
                # 1 0 0
                if grid[i][j] == "/":
                    ext_grid[ext_grid_i][ext_grid_j +2] = 1
                    ext_grid[ext_grid_i + 1][ext_grid_j + 1] = 1 
                    ext_grid[ext_grid_i + 2][ext_grid_j] = 1

        # Count num of regions using flood fill   
        region_count = 0
        for i in range(grid_size * 3):
            for j in range(grid_size * 3):
                # If we find an unvisited cell (0), it's a new region
                if ext_grid[i][j] == 0:
                    # Fill that region
                    self._flood_fill(ext_grid, i, j)
                    region_count += 1

        return region_count



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([" /","/ "], 2),
        ([" /","  "], 1),
        (["/\\","\\/"], 5)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.regionsBySlashes(input), expected)

    
   