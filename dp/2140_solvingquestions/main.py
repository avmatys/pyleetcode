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

# https://leetcode.com/problems/solving-questions-with-brainpower/description/
class Solution:

    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[n - 1] = questions[n - 1][0]
        for i in range(n - 2, -1, -1):
            ni = i + questions[i][1] + 1
            dp[i] = max(questions[i][0] + (dp[ni] if ni < n else 0), dp[i + 1])
        return dp[0]


def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[3,2],[4,3],[4,4],[2,5]], 5)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.mostPoints(input), expected)

    
   
