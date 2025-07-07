from typing import List


class Solution:

    def createSortedArray(self, instructions: List[int]) -> int:

        MOD = 10**9 + 7
        m = max(instructions) + 1
        nums = [0] * m

        def query(x):
            res = 0
            while x > 0:
                res += nums[x]
                x -= x & -x
            return res
        
        def update(x):
            while x < m:
                nums[x] += 1
                x += x & -x

        res = 0
        for i, x in enumerate(instructions):
            res += min(query(x - 1), i - query(x))
            update(x)
        return res % MOD
        
