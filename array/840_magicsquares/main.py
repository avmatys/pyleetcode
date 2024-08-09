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


# https://leetcode.com/problems/4sum/description/
class Solution:

    @timeit
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        magic_squares = [
                            [[4,3,8],[9,5,1],[2,7,6]],
                            [[8,3,4],[1,5,9],[6,7,2]],

                            [[4,9,2],[3,5,7],[8,1,6]],
                            [[2,9,4],[7,5,3],[6,1,8]],

                            [[5,3,2],[1,5,9],[8,7,4]],
                            [[2,3,5],[9,5,1],[4,7,8]],
                            
                            [[6,7,2],[1,5,9],[8,3,4]],
                            [[2,7,6],[9,5,1],[4,3,8]],

                            [[6,1,8],[7,5,3],[2,9,4]],
                            [[8,1,6],[3,5,7],[4,9,2]],

                            [[6,3,2],[1,5,9],[8,7,4]],
                            [[2,3,6],[9,5,1],[4,7,8]],

                            [[8,7,4],[1,5,9],[6,3,2]],
                            [[4,7,8],[9,5,1],[2,3,6]]  
                        ]
        
        grid_row = 0
        grid_col = 0

        count = 0
        while grid_row + 2 < len(grid[0]):
            grid_col = 0
            while grid_col + 2 < len(grid):
                for square in magic_squares:
                    if square[0] == grid[grid_row][grid_col:grid_col+3] \
                        and square[1] == grid[grid_row+1][grid_col:grid_col+3] \
                        and square[2] == grid[grid_row+2][grid_col:grid_col+3]:
                        count += 1
                grid_col += 1
            grid_row += 1

        return count


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[4,3,8,4],[9,5,1,9],[2,7,6,2]], 1),
        ([[9]], 0),
        ([[5,5,5],[5,5,5],[5,5,5]], 0),
        ([[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]], 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.numMagicSquaresInside(input), expected)

    
   