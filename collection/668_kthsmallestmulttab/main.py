from typing import List

class Solution:

    def count_less_x(self, m, n, x):
        res = 0
        for i in range(1, m + 1):
            res += min(x // i, n)
        return res

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l = 1
        r = m * n
        while l < r:
            mid = l + (r - l) // 2
            if k <= self.count_less_x(m, n, mid):
                r = mid
            else:
                l = mid + 1
        return l

