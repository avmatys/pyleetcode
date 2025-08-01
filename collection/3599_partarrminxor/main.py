from typing import List

class Solution:

    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def solve(i, k):
            if i == n:
                return 0
            if n - i < k or k <= 0:
                return float('inf')
            res = float('inf')
            curr = 0
            for j in range(i, n - k + 1):
                curr ^= nums[j]
                if curr < res:
                    next = solve(j + 1, k - 1)
                    res = min(res, max(curr, next))
            return res

        return solve(0, k)
