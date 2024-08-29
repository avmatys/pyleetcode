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


# https://leetcode.com/problems/count-sorted-vowel-strings/description/
class Solution:

    @timeit
    def countVowelStringsRecursion(self, n: int) -> int:
        
        CHAR_COUNT = {'a': 5, 'e': 4, 'i': 3, 'o': 2, 'u': 1}

        def count(n: int, last_char: str):
            # Base case when we shoul specify last char
            if n == 1:
                return CHAR_COUNT[last_char]
            # Other cases - we should get base case in the result
            total = 0
            for char in ['a', 'e', 'i', 'o', 'u']:
                # Chars should be sorted 
                if last_char <= char:
                    total += count(n-1, char)
            return total

        return count(n, 'a')
    
    @timeit
    def countVowelStrings(self, n: int) -> int:
        
        # Base case
        dp = [1, 1, 1, 1, 1]

        # For each next iteration 
        # a -> dp[0] = dp[0] + dp[1] + dp[2] + dp[3] + dp[4]
        # e -> dp[1] = dp[1] + dp[2] + dp[3] + dp[4]
        # i -> dp[2] = dp[2] + dp[3] + dp[4]
        # o -> dp[3] = dp[3] + dp[4]
        # u -> dp[4] = dp[4]
        for i in range(1, n):
            for dp_idx in range(4):
                dp[dp_idx] = sum(dp[dp_idx:])
        return sum(dp)
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [(1, 5),
             (2, 15),
             (3, 35),
             (33, 66045)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.countVowelStringsRecursion(input), expected)
        judge(solution.countVowelStrings(input), expected)

    
   