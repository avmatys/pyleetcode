from typing import List
from datetime import datetime
from collections import Counter


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(symbol):
            return symbol in set("aeiou")
        n = len(s)
        curr_count, max_count = 0, 0
        for i in range(n):
            curr_count += is_vowel(s[i])
            if i >= k:
                curr_count -= is_vowel(s[i-k])
            max_count = max(max_count, curr_count)
        return max_count

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("abciiidef", 3), 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxVowels(*input), expected)

    
   