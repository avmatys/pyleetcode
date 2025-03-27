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

# https://leetcode.com/problems/longest-valid-parentheses/description/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack, dp = [], [0] * n
        for i in range(n):
            if s[i] == ")" and stack:
                dp[stack.pop()] = dp[i] = 1
            if s[i] == "(":
                stack.append(i)
        max_len, curr_len = 0, 0
        for val in dp:
            if val == 0:
                curr_len = 0
            else:
                curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (")()())", 4)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.longestValidParentheses(input), expected)

    
   
