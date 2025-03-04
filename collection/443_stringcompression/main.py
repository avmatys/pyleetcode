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

# https://leetcode.com/problems/string-compression/description/
class Solution:

    @timeit
    def compress(self, chars: List[str]) -> int:
        idx = 0
        i, n = 1, len(chars)
        while i <= n:
            cnt = 1
            while i < n and chars[i-1] == chars[i]:
                cnt += 1
                i += 1
            chars[idx] = chars[i - cnt]
            idx += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[idx] = c
                    idx += 1
            i += 1
        return idx

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (["a","a","b","b","c","c","c"], ["a", "2", "b", "2", "c", "3"]),
        (["a"], ["a"]),
        (["a","b","b","b","b","b","b","b","b","b","b","b","b"], ["a","b","1","2"])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        size = solution.compress(input)
        judge(input[:size], expected)
   