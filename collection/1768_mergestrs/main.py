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


# https://leetcode.com/problems/merge-strings-alternately/
class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i, j = 0,0
        result = []
        while i < n or j < m:
            if i < n:
                result.append(word1[i])
                i+=1
            if j < m:
                result.append(word2[j])
                j+=1
        return "".join(result)

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("abc", "pqr"), "apbqcr"),
        (("ab", "pqrs"), "apbqrs"),
        (("abc", "pq"), "apbqc")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.mergeAlternately(*input), expected)