from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        dp = [defaultdict(int) for _ in nums]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                res = max(res, dp[i][diff])
        return res
