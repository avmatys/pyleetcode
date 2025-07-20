from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n + 1)
        for start,end,direction in shifts:
            offset = 1 if direction else -1
            prefix[start] += offset
            prefix[end+1] -= offset
        csum = 0
        res = []
        for i in range(n):
            csum = (csum + prefix[i]) % 26
            cidx = ord(s[i]) - ord('a')
            res.append(chr(ord('a') + (cidx + csum) % 26))
        return "".join(res)
