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


# https://leetcode.com/problems/maximum-gap/description/
class Solution:

    @timeit
    def maximumGap(self, nums: List[int]) -> int:
        
        n = len(nums)
        low, high = min(nums), max(nums)

        if n <= 2 or high == low:
            return high - low
        
        buckets = [[] for _ in range(n-1)]

        for num in nums:
            idx = (num - low) * (n - 1) // (high - low)
            if num == high:
                idx = n - 2
            buckets[idx].append(num)
        
        candidates = []
        for bucket in buckets:
            if not bucket:
                continue
            candidates.append([min(bucket), max(bucket)])

        max_value = 0
        for i in range(1, len(candidates)):
            curr_value = candidates[i][0] - candidates[i - 1][1]
            if curr_value > max_value:
                max_value = curr_value
        
        return max_value


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
             ([3,14,15,83,6,4,19,20,40], 43),
             ([1,1,1,1,1,5,5,5,5,5], 4),
             ([3,6,9,1], 3),
             ([10], 0)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maximumGap(input), expected)

    
   