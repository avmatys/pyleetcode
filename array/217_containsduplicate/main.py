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

# https://leetcode.com/problems/contains-duplicate/description
class Solution:

    @timeit
    def containsDuplicate(self, nums: List[int]) -> bool:
        existing = set()
        for num in nums:
            if num in existing:
                return True
            existing.add(num)
        return False
    
    @timeit
    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3,1], True),
        ([4,3,2,1,5], False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.containsDuplicate(input), expected)
        judge(solution.containsDuplicate2(input), expected)

    
   