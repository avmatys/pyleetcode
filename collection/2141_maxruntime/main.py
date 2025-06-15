from typing import List

class Solution:

    def can_power(self, bat, n, k):
        target = n * k
        bsum = sum([min(b,k) for b in bat])
        return bsum >= target

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        l = 1
        r = total // n + 1
        while l < r:
            m = l + (r - l) // 2
            if self.can_power(batteries, n, m):
                l = m + 1
            else:
                r = m
        return l - 1

