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


# https://leetcode.com/problems/broken-calculator/description/
class Solution:

    def brokenCalc(self, start: int, target: int) -> int:
        count = 0
        while target != start:
            if target > start:
                if target % 2 == 0:
                    target /= 2
                else:
                    target += 1
                count += 1
            else:
                count += int(start - target)
                target = start
        return count


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((2,3), 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.brokenCalc(*input), expected)

    
   
