from typing import List
from datetime import datetime
import sys

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/third-maximum-number/
class Solution:

    @timeit
    def thirdMax(self, nums: List[int]) -> int: 
        MIN = -sys.maxsize - 1
        fmax = MIN
        smax = MIN
        tmax = MIN
        for num in nums:
            if num > fmax:
                tmax = smax
                smax = fmax
                fmax = num
            elif num < fmax and num > smax:
                tmax = smax
                smax = num
            elif num < smax and num > tmax:
                tmax = num

        answer = tmax
        if tmax == MIN:
            answer = fmax
        return answer
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3,2,1],1),
        ([1,2], 2),
        ([2,2,3,1], 1),
        ([1,2,2,5,3,5], 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.thirdMax(input), expected)


    
   