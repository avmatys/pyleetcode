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

# https://leetcode.com/problems/new-21-game/description/
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
        maxPts = 4
        dp[0] = 1
        dp[1] = 0.25 = dp[0] * 1/maxPts
        dp[2] = 0.25 + (0.25 * 0.25) = (dp[0] + dp[1]) * 1/maxPts =  0.3125 
        dp[3] = 0.25 + (0.25 * 0.25 * 0.25) + (0.25 * 0.25) + (0.25 * 0.25) = (dp[0] + dp[1] + dp[2]) * 1/maxPts = 0.390625
        dp[4] = (dp[0] + dp[1] + dp[2] + dp[3]) * 1/maxPts = 0.48828125
        dp[5] = (dp[1] + dp[2] + dp[3] + dp[4]) * 1/maxPts = 0.36035156625
        dp[6] = (dp[2] + dp[3] + dp[4] + dp[5]) * 1/maxPts = 0.XXXXXX
        """
        if k == 0 or n - k + 1 >= maxPts:
            return 1.0
        res = 0
        dp = [0] * (n + 1)
        dp[0] = 1
        s = 1
        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i >= maxPts:
                s -= dp[i - maxPts]
        return sum(dp[k:])  
        
