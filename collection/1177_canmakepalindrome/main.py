from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        pref = [0] * (n + 1)
        for i in range(n):
            k = ord(s[i]) - ord('a')
            pref[i + 1] = pref[i] ^ (1 << k)
        res = []
        for l, r, k in queries:
            res.append(bin(pref[r + 1] ^ pref[l]).count('1') // 2 <= k)
        return res
