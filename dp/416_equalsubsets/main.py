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


# https://leetcode.com/problems/partition-equal-subset-sum/description/
class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        dp = [False] * (target_sum + 1)
        dp[0] = True
        for num in nums:
            for curr_sum in range(target_sum, num - 1, -1):
                dp[curr_sum] |= dp[curr_sum - num]
        return dp[target_sum]


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,5,11,5], True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.canPartition(input), expected)

    
   
