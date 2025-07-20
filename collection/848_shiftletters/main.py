from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        csum = 0
        n = len(shifts)
        res = [""] * n
        for i in range(n - 1, -1, -1):
            csum = (csum + shifts[i]) % 26 
            cidx = ord(s[i]) - ord('a')
            res[i] = chr((cidx + csum) % 26 + ord('a'))
        return "".join(res)
