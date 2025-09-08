from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.total = sum(nums)
        self.res = 0
        self.memo = [[float('-inf')] * (2 * self.total + 1)  for _ in range(n)]

        def helper(idx, curr):
            if idx == n:
                return int(curr == target)
            if self.memo[idx][curr + self.total] != float('-inf'):
                return self.memo[idx][curr + self.total]
            # Plus
            add = helper(idx + 1, curr + nums[idx])
            # Subtract
            subtract = helper(idx + 1, curr - nums[idx])
            # Store in memo
            self.memo[idx][curr + self.total] = add + subtract
            return self.memo[idx][curr + self.total]

        return helper(0, 0)

