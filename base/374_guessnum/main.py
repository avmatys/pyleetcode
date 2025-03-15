from typing import List
from datetime import datetime
from typing import Optional
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

# https://leetcode.com/problems/guess-number-higher-or-lower/description
class Solution:

    def guessNumber(self, n: int) -> int:
        left, right  = 0, n
        while left <= right:
            middle = (left + right) // 2
            response = guess(middle)
            if response == 0:
                return middle
            elif response == -1:
                right = middle - 1
            else:
                left = middle + 1


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
