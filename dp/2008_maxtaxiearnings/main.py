from typing import List

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        m = len(rides)
        rides.sort(key=lambda x: x[0])
        starts = [s for s, _, _ in rides]
        dp = [0] * (m + 1)
        for ci in range(m - 1, -1, -1):
            ni = bisect.bisect_right(starts, rides[ci][1] - 1)
            dp[ci] = max(dp[ci + 1], rides[ci][1] - rides[ci][0] + rides[ci][2] + dp[ni])
        return dp[0]
