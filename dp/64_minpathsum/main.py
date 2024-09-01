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


# https://leetcode.com/problems/minimum-path-sum/description/
class Solution:

    @timeit
    def minPathSum(self, grid: List[List[int]]) -> int:

        row_count = len(grid)
        column_count = len(grid[0])

        # Start dp
        dp = [[1000000 for _ in range(column_count)] for _ in range(row_count)]
        dp[0][0] = grid[0][0]

        # Init dp array with values from grid
        for i in range(1, row_count):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, column_count):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Start dp
        for i in range(1, row_count):
            for j in range(1, column_count):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[row_count - 1][column_count - 1]

    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[1,3,1],[1,5,1],[4,2,1]], 7),
        ([[1,2,3],[4,5,6]], 12)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minPathSum(input), expected)

    
   