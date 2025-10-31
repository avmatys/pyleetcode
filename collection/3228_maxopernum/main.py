from typing import List

class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        res = 0
        cnt = 0
        i = 0
        while i < n:
            while i < n and s[i] == '1':
                cnt += 1
                i += 1
            zeroes = 0
            while i < n and s[i] == '0':
                zeroes += 1
                i += 1
            if zeroes > 0:
                res += cnt
        return res
