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


# https://leetcode.com/problems/distribute-candies/description/
class Solution:

    def distributeCandies(self, candyType: List[int]) -> int:
        return int(min(len(candyType) / 2, len(set(candyType))))


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,1,2,2,3,3], 3),
        ([1,1,2,3], 2),
        ([6,6,6,6], 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.distributeCandies(input), expected)

    
   