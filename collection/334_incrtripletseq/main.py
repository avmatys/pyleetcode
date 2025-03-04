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


# https://leetcode.com/problems/increasing-triplet-subsequence/description/
class Solution:

    @timeit
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = num2 = float('inf')
        for num in nums:
            if num <= num1:
                num1 = num
            elif num <= num2:
                num2 = num
            else:
                return True
        return False    


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
                ([2,1,5,0,5,6], True),
                ([1,5,0,4,1,3], True),
                ([20,100,10,12,5,13], True),
                ([5,3,2,1], False)
            ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.increasingTriplet(input), expected)

   
    