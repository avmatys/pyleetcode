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


# https://leetcode.com/problems/maximum-repeating-substring/description/
class Solution:

    @timeit
    def maxRepeating(self, sequence: str, word: str) -> int:
        seq_len = len(sequence)
        words_len = len(word)
        dp = [0] * (seq_len + 1)
        max_group_count = 0
        for i in range (words_len, seq_len + 1):
            if sequence[i-words_len: i] == word:
                dp[i] = dp[i-words_len] + 1
                max_group_count = max(max_group_count, dp[i])
        return max_group_count
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("ababc", "ab"), 2),
        (("ababc", "ba"), 1), 
        (("ababc", "ac"), 0), 
        (("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"), 5)
    ]
    
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxRepeating(input[0], input[1]), expected)

    
   