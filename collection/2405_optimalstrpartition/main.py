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

# https://leetcode.com/problems/optimal-partition-of-string/description/
class Solution:
    def partitionString(self, s: str) -> int:
        seen = 0
        result = 1
        for ch in s:
            mask = 1 << (ord(ch) - 97)
            if seen & mask:
                seen = 0
                result += 1
            seen |= mask
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ("abacaba", 4)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.partitionString(input), expected)
    
   
