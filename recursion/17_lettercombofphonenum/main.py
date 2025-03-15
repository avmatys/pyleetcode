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


# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:

    @timeit
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        size = len(digits)
        if size == 0:
            return result
        def combine(letters, idx):
            if idx == size:
                result.append(''.join(letters))
                return
            for char in keyboard[digits[idx]]:
                letters.append(char)
                combine(letters, idx + 1)
                letters.pop()
        combine([], 0)
        return result

class SolutionRev:
    def permutate(self, digits, result, path, idx):
        if idx == len(digits):
            result.append("".join(path))
            return
        keyboard = {
            "2": "abc", "3": "def", "4": "ghi","5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv","9": "wxyz"
        }
        for ch in keyboard[digits[idx]]:
            path.append(ch)
            self.permutate(digits, result, path, idx + 1)
            path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) > 0:
            self.permutate(digits, result, [], 0)
        return result
        
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.letterCombinations(input), expected)

    
   
