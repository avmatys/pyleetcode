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


# https://leetcode.com/problems/find-the-highest-altitude/description/ 
class Solution:

    @timeit
    def largestAltitude(self, gain: List[int]) -> int:
        max_height = 0
        curr_height = 0
        for g in gain:
            curr_height += g
            max_height = max(max_height, curr_height)
        return max_height

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([-5,1,5,0,-7], 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.largestAltitude(input), expected)

    
   