from typing import List

class Solution:

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:

        n = len(nums)
        memo = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

        def solve(start, k):
            if start >= n or memo[k][start] > 0: 
                return memo[k][start]
            csum = 0
            for i in range(start, n - k + 1):
                csum += nums[i]
                # For the latest group sum up elements and not try to split
                if k == 1 and i < n - 1: 
                    continue
                cavg = csum / (i - start + 1) + solve(i + 1, k - 1)
                memo[k][start] = max(memo[k][start], cavg)
            return memo[k][start]
        
        solve(0, k)
        return memo[k][0]
