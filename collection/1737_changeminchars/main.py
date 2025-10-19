from typing import List

class Solution:
    def minCharacters(self, s1: str, s2: str) -> int:

        def opt1(f1, f2):
            res = float('inf')
            for i in range(1, 26):
                res = min(res, f1[i] + f2[26] - f2[i])
            return res

        def opt2(f1, f2):
            return opt1(f2, f1)

        def opt3(n1, n2, f1, f2):
            return (n1 - max(f1)) + (n2 - max(f2))

        n1, n2 = len(s1), len(s2)
        f1, f2 = [0] * 26, [0] * 26
        for ch in s1:
            f1[ord(ch) - ord('a')] += 1
        for ch in s2:
            f2[ord(ch) - ord('a')] += 1
        p1, p2 = [0] * 27, [0] * 27
        for i in range(1, 27):
            p1[i] = p1[i-1] + f1[i-1]
            p2[i] = p2[i-1] + f2[i-1]
        return min(opt1(p1, p2), opt2(p1, p2), opt3(n1, n2, f1, f2))

