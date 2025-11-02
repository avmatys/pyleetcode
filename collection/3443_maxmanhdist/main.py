from typing import List

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 0
        for direction in ['NW', 'NE', 'SW', 'SE']:
            dv, dh = direction
            ct, ck = 0, k
            for ch in s:
                if ch == dv or ch == dh or ck > 0:
                    ct += 1
                elif ck > 0:
                    ct += 1
                    ck -= 1
                else:
                    ct -= 1
                res = max(res, ct)
        return res
