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


# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
class Solution:

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [cnt + extraCandies >= max(candies) for cnt in candies]

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([2,3,5,1,3], 3), [True, True, True, False, True])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.kidsWithCandies(*input), expected)

    
   