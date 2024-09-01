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


# https://leetcode.com/problems/decode-ways/description/
class Solution:

    @timeit
    def numDecodings(self, s: str) -> int:
        
        # Simple basic checks
        if s[0] == '0':
            return 0

        str_length = len(s)
        if str_length == 1:
            return 1
        
        # Start dp
        dp = [0] * (str_length + 1)
        dp[0] = dp[1] = 1
        
        for i in range(2, str_length + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2: i])

            if one_digit > 0:
                dp[i] += dp[i - 1]

            if 9 < two_digits < 27:
                dp[i] += dp[i - 2]

        return dp[str_length]

    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("12", 2),
        ("226", 3),
        ("11106", 2),
        ("111111111111111111111111111111111111111111111", 1836311903)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.numDecodings(input), expected)

    
   