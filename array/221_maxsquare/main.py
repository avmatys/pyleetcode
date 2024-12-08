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


# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for j in range(cols):
            dp[0][j] = int(matrix[0][j])
        for i in range(rows):
            dp[i][0] = int(matrix[i][0])
        for i in range (1, rows):
            for j in range(1, cols):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        result = 0
        for i in range(rows):
            result = max(*dp[i], result)
        return result*result




def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4),
        ([["0","1"],["1","0"]], 1),
        ([["0"]], 0)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maximalSquare(input), expected)

    
   