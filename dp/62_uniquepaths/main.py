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


# https://leetcode.com/problems/unique-paths/
class Solution:

    @timeit
    def uniquePaths(self, m: int, n: int) -> int:
       
        row_count = m
        column_count = n
        dp = [[1 for _ in range(column_count)] for _ in range(row_count)]

        for i in range(1, row_count):
            for j in range(1, column_count):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[row_count-1][column_count-1]


class SolutionRev:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ((3, 7), 28),
                ((3, 2), 3)  
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.uniquePaths(input[0], input[1]), expected)

    
   
