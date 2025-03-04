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


# https://leetcode.com/problems/plus-one/description/
class Solution:

    @timeit
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)
        while i >= 0:
            i -= 1
            # Check one by one digit
            if digits[i] == 9:
                digits[i] = 0
                # Add one in the beginning and stop
                if i == 0:
                    digits = [1] + digits
                    break
            # If not nine - increment and stop
            else:
                digits[i] += 1
                break
        return digits


def judge(nums, expected_nums):
    print(f'Nums {nums} Expected {expected_nums}')
    for i in range(len(nums)):
        assert nums[i] == expected_nums[i]
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3],[1,2,4]),
        ([0],[1]),
        ([9], [1,0]),
        ([9,9,8], [9,9,9]),
    ]
    for case in cases:
        print("Solution 1")
        nums = case[0].copy()
        expected_nums = case[1]
        judge(solution.plusOne(nums), expected_nums)

    
   