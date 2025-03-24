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


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n, total = len(possible), 0
        for i in range(n):
            if possible[i] == 0:
                possible[i] -= 1
            total += possible[i]
        accum = 0
        for i in range(n - 1):
            accum += possible[i]
            if 2 * accum > total:
                return i + 1
        return -1       


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,0,1,0], 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minimumLevels(input), expected)

    
   
