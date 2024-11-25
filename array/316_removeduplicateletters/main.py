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


# https://leetcode.com/problems/remove-duplicate-letters/
class Solution:

    @timeit
    def removeDuplicateLetters(self, s: str) -> str:

        result = [] # Result set which acts as a stack
        visited = set() # Stores chars which are in the stack for quick check
        lastIdx = [-1] * 26 # Store idx of each character in the initial string
        
        for i, ch in enumerate(s):
            lastIdx[ord(ch) - ord('a')] = i

        for i, ch in enumerate(s):
            if ch in visited:
                continue
            while result and result[-1] > ch and i < lastIdx[ord(result[-1]) - ord('a')]:
                visited.remove(result.pop())           
            visited.add(ch)
            result.append(ch) 

        return ''.join(result)

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
             ("bcabc", "abc"),
             ("cbacdcbc", "acdb")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.removeDuplicateLetters(input), expected)

    
   