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

# https://leetcode.com/problems/majority-element/description
class Solution:

    @timeit
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore Majority Algorithm
        counter = 0
        majority_element = 0
        for num in nums:
            if counter == 0:
                majority_element = num
                counter += 1
            elif majority_element == num:
                counter += 1
            else:
                counter -= 1
        return majority_element
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([2,2,1], 2),
        ([4,1,2,2,1,2], 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.majorityElement(input), expected)

    
   