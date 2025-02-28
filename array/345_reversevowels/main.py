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

# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
class Solution:

    @timeit
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowels = set("aAiIeEuUoO")
        chars = list(s)
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            chars[left], chars[right] = chars[right], chars[left]
            left, right = left + 1, right - 1
        return "".join(chars)
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("IceCreAm","AceCreIm"),
        ("IcmCrmmm","IcmCrmmm"),
        ("mmmmmmmm","mmmmmmmm"),
        ("ammmmmma","ammmmmma"),
        ("mmmammmm","mmmammmm"),
        ("mmmaimmm","mmmiammm")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.reverseVowels(input), expected)


    
   