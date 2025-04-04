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


# https://leetcode.com/problems/regular-expression-matching/description/
class Solution:

    def isMatch(self, s: str, pattern: str) -> bool:
        m, n = len(s), len(pattern)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        # Calc first row of dp array
        for j in range(1, n + 1):
            if pattern[j - 1] == '*':
                dp[0][j] = dp[0][j-2]
        # Calc different patterns
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[j-1] == "*":
                    dp[i][j] = dp[i][j-2]
                    if not dp[i][j] and pattern[j-2] in {s[i-1], '.'}:
                        dp[i][j] = dp[i-1][j]
                elif pattern[j-1] in {s[i-1], '.'}:
                    dp[i][j] = dp[i-1][j-1]
        return dp[m][n]        
        

def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("aa", "a"), False),
        (("aa", "a*"), True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.isMatch(*input), expected)

    
   
