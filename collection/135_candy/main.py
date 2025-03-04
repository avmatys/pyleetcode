from typing import List
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/candy/description/
class Solution:

    @timeit
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                result[i] = max(result[i + 1] + 1, result[i])
        return sum(result)
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,0,2], 5),
        ([1,1,1], 3),
        ([1,2,2], 4),
        ([1,3,4,5,2], 11),
        ([0,1,5,3,2,1], 13)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.candy(input), expected)


    
   