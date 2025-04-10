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


# https://leetcode.com/problems/count-the-number-of-powerful-integers/description/
class Solution:

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
       
        def count_nums(bound: str):
            if len(bound) < len(s):
                return 0
            if len(bound) == len(s):
                return int(bound >= s)
            count = 0
            prefix_len = len(bound) - len(s)
            for i in range(prefix_len):
                if int(bound[i]) > limit:
                    count += (limit + 1) ** (prefix_len - i)
                    return count
                count += int(bound[i]) * (limit + 1) ** (prefix_len - i - 1)
            if bound[prefix_len: ] >= s:
                count += 1
            return count

        return count_nums(str(finish)) - count_nums(str(start - 1))
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((1,6000,4, "124"), 5)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.numberOfPowerfulInt(*input), expected)

    
   
