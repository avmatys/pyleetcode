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


# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:

    @timeit
    # Slow approach
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)] # dp[i][j] has True, if substr[i:j] is a palindrome (including bounds)
        substr_idxs = (0, 0) # Set as an anser first symbol

        # Each symbol is a palindrome by default
        for i in range(n):
            dp[i][i] = True

        # Check if 2 same symbols are stored in the middle of the palindrome
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                substr_idxs = (i, i + 1)

        # Start check if substring of the len 3 and more is a palindrome
        for substr_len in range(2, n):
            for i in range(n - substr_len):
                j = i + substr_len
                if s[i] == s[j] and dp[i + 1][j - 1] == True: # Result for the prev palindrome is stored in next row and prev column
                    dp[i][j] = True
                    substr_idxs = (i, j)

        # Get substring
        i, j = substr_idxs
        return s[i : j + 1]
    

    # Better approach
    def longestPalindrome2(self, s: str) -> str:
        
        n = len(s)

        # Check if we have a palindrome near the center
        # Center can be 2 same symbols, that's why we have 2 params - left and right
        def expand(left: int, right: int) -> int:
            left_idx = left
            right_idx = right
            while left_idx >= 0 and right_idx < n and s[left_idx] == s[right_idx]:
                left_idx -= 1
                right_idx += 1
            return right_idx - left_idx - 1 # Length of the substr

        # Process each symbol as a center
        answer = (0,0) # Set first as a default value
        for i in range(n):
            # Odd
            odd_len = expand(i, i)
            curr_len = answer[1] - answer[0] + 1
            if odd_len > curr_len:
                radius = odd_len // 2
                answer = (i - radius, i + radius)
            # Even
            even_len = expand(i, i + 1)
            curr_len = answer[1] - answer[0] + 1
            if even_len > curr_len:
                radius = (even_len // 2) - 1
                answer = (i - radius, i + radius + 1)
        
        # Get substring
        i, j = answer
        return s[i : j + 1]


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ("babac", "bab"),
                ("cbbd", "bb")
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.longestPalindrome2(input), expected)

    
   