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


# https://leetcode.com/problems/maximum-average-subarray-i/description/
class Solution:

    @timeit
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, n):
            window_sum += (nums[i] - nums[i-k])
            max_sum = max(max_sum, window_sum)
        return max_sum / k


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,12,-5,-6,50,3], 4), 12.75)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.findMaxAverage(*input), expected)

   
    