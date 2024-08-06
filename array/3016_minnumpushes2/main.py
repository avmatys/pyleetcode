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


# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/?envType=daily-question&envId=2024-08-06
class Solution:

    @timeit
    def minimumPushes(self, word: str) -> int:
        # Basic case
        if len(word) <= 8:
            return len(word)
        
        # Calc frequency of the each char in the alphabet
        char_frequency = [0] * 26
        for char in word:
            idx = ord(char) - 97
            char_frequency[idx] += 1
        
        # Sort in a reverse order
        char_frequency.sort(reverse=True)

        # Count total price
        total = 0
        for i in range(len(char_frequency)):
            total += (i//8 + 1) * char_frequency[i]
        
        return total


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("afhtgpque",10),
        ("alporfmdqsbhncwyu", 27),
        ("xyzxyzxyzxyz",12),
        ("aabbccddeeffgghhiiiiii", 24),
        ("aabbccddeeffgghhiiiiiimmmm", 30),
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minimumPushes(input), expected)

    
   