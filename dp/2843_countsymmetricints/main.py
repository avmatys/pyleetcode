from typing import List
from datetime import datetime
from functools import cache

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/count-symmetric-integers/description/
class Solution:

    def countSymmetricIntegers(self, low: int, high: int) -> int:

        # Params:
        # bound - upper bound value str(int) - used to check which max digit can be used at every position
        # idx - current analyzed idx in the bound.
        # start - position, from which we started building a number
        # diff - stores the difference be
        @cache
        def dfs(bound: str, idx: int, start: int, diff: int, is_limit: bool, is_num: bool):
            # We reached to the latest digit in the string - base case
            if idx >= len(bound):
                return int(is_num and diff == 0)
            # Cases, where value should be calculated
            # 1 We can skip any digit
            result = 0
            if not is_num:
                result += dfs(bound, idx + 1, start, diff, False, False)
            # 2 We have already started a num or we want to start a num
            # We can start a num in the case, when the remaining length is even only
            if is_num or (len(bound) - idx) % 2 == 0:
                # We haven't started a num yet
                if start == -1:
                    start = idx
                lower_digit = 0 if is_num else 1
                upper_digit = int(bound[idx]) if is_limit else 9
                first_part = idx < (len(bound) - 1 + start) / 2
                # We will try to form a digit sequence with each available digit
                for digit in range(lower_digit, upper_digit + 1):
                    next_diff = diff + digit if first_part else diff - digit
                    result += dfs(bound, idx + 1, start, next_diff, is_limit and digit == upper_digit, True)
            return result

        # Trigger calculation of number of items
        return dfs(str(high), 0, -1, 0, True, False) - dfs(str(low - 1), 0, -1, 0, True, False)


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((1200, 1230), 4)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.countSymmetricIntegers(*input), expected)

    
   
