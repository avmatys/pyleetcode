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


# https://leetcode.com/problems/largest-divisible-subset/description/?envType=daily-question&envId=2025-04-06
class Solution:

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        path = [-1] * n
        maxi = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    path[i] = j
            if dp[maxi] < dp[i]:
                maxi = i
        result = []
        i = maxi
        while i >= 0:
            result.append(nums[i])
            i = path[i]
        result.reverse()
        return result
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
	([1,2,4,8], [1,2,4,8])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.largestDivisibleSubset(input), expected)

    
   
