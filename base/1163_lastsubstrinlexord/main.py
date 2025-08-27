from typing import List

class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i, j, k = 0, 1, 0
        while j + k < n:
            if s[i+k] == s[j+k]:
                k += 1
                continue
            elif s[i+k] > s[j+k]:
                j += k + 1
            else:
                i = max(i+k+1, j)
                j = i + 1
            k = 0
        return s[i:]
