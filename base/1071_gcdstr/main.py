from typing import List
from datetime import datetime
from collections import deque
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


# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
class Solution:

    @timeit
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        template = str2 if len(str1) < len(str2) else str2
        for i in range(len(template), 0, -1):
            prefix = template[:i]
            str1_i = len(str1)
            while str1_i > 0 and str1[str1_i-i : str1_i] == prefix:
                str1_i -= i
            if str1_i > 0:
                continue
            str2_i = len(str2)
            while str2_i > 0 and str2[str2_i - i : str2_i] == prefix:
                str2_i -= i
            if str2_i == 0:
                return prefix
        return ''

    @timeit
    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        def gcd(a,b):
            return b if a == 0 else gcd(b % a, a)
        return str1[:gcd(len(str1), len(str2))]
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (('ab', 'ab'), 'ab'),
        (('ab', 'abab'), 'ab'),
        (('ab', 'abba'), ''),
        (('abab', 'a'), ''),
        (('abab', 'abababab'), 'abab'),
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.gcdOfStrings(*input), expected)
        judge(solution.gcdOfStrings2(*input), expected)

    
   