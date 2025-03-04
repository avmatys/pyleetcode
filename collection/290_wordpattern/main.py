from typing import List
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/word-pattern/description/
class Solution:

    @timeit
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False
        word_map = {}
        for i in range(len(words)):
            if words[i] not in word_map:
                word_map[words[i]] = pattern[i]
            elif word_map[words[i]] != pattern[i]:
                return False
        return True
        
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("abba", "dog cat cat dog"), True),
        (("abba", "dog cat cat dog2"), False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.wordPattern(*input), expected)


    
   