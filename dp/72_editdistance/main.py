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


# https://leetcode.com/problems/edit-distance/description/
class Solution:

    @timeit
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2: return 0
        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0: 
                    dp[i][j] = j
                elif j == 0: 
                    dp[i][j] = i 
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
        return dp[n][m]
    
def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("zoologicoarchaeologist", "zoogeologist"), 10),
        (("horse", "ros"), 3),
        (("intention", "execution"), 5)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minDistance(*input), expected)

    
   