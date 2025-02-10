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


# https://leetcode.com/problems/interleaving-string/description/
class Solution:

    @timeit
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if len(s3) != n + m:
            return False
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        # Check s1
        for i in range(1, n + 1):
            if s3[i-1] == s1[i-1] and dp[i-1][0]:
                dp[i][0] = True
        # Check s2
        for j in range(1, m + 1):
            if s3[j-1] == s2[j-1] and dp[0][j-1]:
                dp[0][j] = True
        # Build dp
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s3[i+j-1] == s1[i-1] and dp[i-1][j]:
                    dp[i][j] = True
                if s3[i+j-1] == s2[j-1] and dp[i][j-1]:
                    dp[i][j] = True
        # Return an answer
        return dp[n][m]

def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("aabc", "abad", "aabadabc"), True),
        (("aabcc", "dbbca", "aadbbcbac"), False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.isInterleave(*input), expected)

    
   