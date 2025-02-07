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


# https://leetcode.com/problems/add-binary/description/
class Solution:

    @timeit
    def addBinary(self, a: str, b: str) -> str:
        idx_a = len(a) - 1
        idx_b = len(b) - 1
        carry, res = 0, []
        while idx_a >= 0 or idx_b >= 0 or carry > 0:
            sum = carry
            if idx_a >= 0: sum += ord(a[idx_a]) - ord('0')
            if idx_b>= 0: sum += ord(b[idx_b]) - ord('0')
            idx_a, idx_b = idx_a - 1, idx_b - 1
            carry = 1 if sum > 1 else 0
            res.append(str(sum % 2))
        return ''.join(reversed(res))

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (("11", "1"), "100"),
        (("1010", "1011"), "10101")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.addBinary(*input), expected)

    
   