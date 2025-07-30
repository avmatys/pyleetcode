from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        for i in range(32):
            mask = 1 << i
            if n & mask > 0:
                powers.append(mask)
        res = []
        for l, r in queries:
            curr = 1
            while l <= r:
                curr = (curr * powers[l]) % (10**9 + 7)
                l += 1
            res.append(curr)
        return res
