from typing import List
from datetime import datetime
from functools import cmp_to_key


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/largest-number/description/
class Solution:

    @timeit
    def largestNumber(self, nums: List[int]) -> str:

        def compare(a: str, b: str):
            return a + b > b + a
        
        n = len(nums)
        for i in range(n):
            nums[i] = str(nums[i])
        
        nums.sort(key=lambda x: x*10, reverse=True)
        
        if nums[0] == "0":
            return "0"

        number = "".join(nums)
        return number

            

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([10,2]), "210"),
        (([3,30,34,5,9]), "9534330")  
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.largestNumber(input), expected)


    
   