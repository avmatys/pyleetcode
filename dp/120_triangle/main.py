from typing import List
from typing import Optional
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


# https://leetcode.com/problems/triangle/description/
class Solution:

    @timeit
    def minimumTotal(self, triangle: List[List[int]]) -> int:
       
        n = len(triangle)
        dp = [[100000000 for _ in range(n)] for _ in range(n)]

        # Set base for the dp
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i + 1):
                # First column can be calculated from the cell above
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                # Last column can be calculated from the cell, which is located left
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                # Simple case - cell above or left one
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

        return min(dp[n-1])


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
        ([[-1],[2,3],[1,-1,-3]], -1),
        ([[-1],[3,2],[1,-2,-1]], -1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minimumTotal(input), expected)

    
   