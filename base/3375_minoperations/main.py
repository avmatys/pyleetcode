from typing import List
from datetime import datetime
from collections import deque

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/?envType=daily-question&envId=2025-04-09
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        bits = 0
        for num in nums:
            bits |= 1 << num
            if num < k:
                return -1
        return bits.bit_count() - ((bits & 1 << k) > 0)


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([5,2,5,4,5], 2), 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minOperations(*input), expected)

    
   
