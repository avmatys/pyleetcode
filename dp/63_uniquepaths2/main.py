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


# https://leetcode.com/problems/unique-paths-ii/
class Solution:

    @timeit
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
       
        row_count = len(obstacleGrid)
        column_count = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[row_count-1][column_count-1] == 1:
            return 0
        
        dp = [[0 for _ in range(column_count)] for _ in range(row_count)]
        dp[0][0] = 1 # We checked what first element is correct one

        for i in range(row_count):
            for j in range(column_count):
                # Mark element as non-reachable (array was inited with 0)
                if obstacleGrid[i][j] == 1:
                    continue
                # Handle first row and column (execpt [0][0] element)
                if i == 0 and j > 0: 
                    dp[i][j] = dp[i][j-1]
                if j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j]
                # Calc other cases
                if i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[row_count-1][column_count-1]
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ([[0,0,0],[0,1,0],[0,0,0]], 2),
                ([[0,1],[0,0]], 1),
                ([[0,0],[1,1],[0,0]], 0)
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.uniquePathsWithObstacles(input), expected)

    
   