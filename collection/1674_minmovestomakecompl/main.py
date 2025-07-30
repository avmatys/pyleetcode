from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2*limit + 2)
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - i - 1]
            # By default we need 2 operations to make a min possible value
            diff[2] += 2
            # We need 1 less operation to make a value [min(a,b) + 1, a + b - 1]
            diff[min(a, b) + 1] -= 1
            # We need 0 operataiona to make a + b
            diff[a + b] -= 1
            # We need 1 more operation to make [a+b+1, max(a,b) + limit]
            diff[a + b + 1] += 1
            # We need 1 more operation to make [max(a, b) + limit + 1, +~]
            diff[max(a,b) + limit + 1] += 1
        curr = 0
        res = n
        for i in range(2, limit * 2 + 1):
            curr += diff[i]
            res = min(res, curr)
        return res

