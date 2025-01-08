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

# https://leetcode.com/problems/zigzag-conversion
class Solution:

    @timeit
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [[] for _ in range(numRows)]
        current_row = 0
        direction = 1
        for i in range(len(s)):
            result[current_row].append(s[i])
            if current_row == 0:
                direction = 1
            if current_row == numRows - 1:
                direction = -1
            current_row += direction
        result = ["".join(res) for res in result]
        return "".join(result)


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("PAYPALISHIRING", 3),"PAHNAPLSIIGYIR"),
        (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
        (("ABC", 1), "ABC")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.convert(*input), expected)


    
   