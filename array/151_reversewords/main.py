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

# https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution:

    @timeit
    def reverseWords(self, s: str) -> str:
        n = len(s)
        left = right = n - 1
        result = []
        while right >= 0 and left >= 0:
            # End of the string
            if s[right] == ' ':
                right -= 1
                continue
            left = right
            # Start of the string
            while left >= 0:
                if left == 0 or s[left] == ' ':
                    result.append(s[left if s[left] != ' ' else left + 1:right + 1])
                    left -= 1
                    right = left
                    break
                left -= 1
        return " ".join(result)


class SolutionRevised:

    @timeit
    def reverseWords(self, s: str) -> str:
        n = len(s)
        left, right = n - 1, n - 1
        result = []
        while left > -1 and right > -1:
            while right > -1 and s[right] == ' ':
                right -= 1
            if right < 0:
                break
            left = right
            while left > -1 and s[left] != ' ':
                left -= 1
            result.append(s[left + 1 : right + 1])
            right = left - 1
        return " ".join(result)
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    solutionRev = SolutionRevised()
    cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        (" a good   example", "example good a")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.reverseWords(input), expected)
        judge(solutionRev.reverseWords(input), expected)


    
   