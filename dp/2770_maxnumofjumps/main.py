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

# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index
class Solution:

    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for i in range(n):
            if dp[i] == -1:
                continue
            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        return dp[n-1]
        

def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,3,6,4,1,2], 2), 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maximumJumps(*input), expected)

    
   
