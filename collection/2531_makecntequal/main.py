from typing import List

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:

        def compare(f1, f2):
            c1 = sum(int(f1[i] > 0) for i in range(26))
            c2 = sum(int(f2[i] > 0) for i in range(26))
            return c1 == c2

        f1 = [0] * 26
        f2 = [0] * 26
        for ch in word1:
            f1[ord(ch) - ord('a')] += 1
        for ch in word2:
            f2[ord(ch) - ord('a')] += 1
        for i in range(26):
            if f1[i] == 0:
                continue
            for j in range(26):
                if f2[j] == 0:
                    continue
                f1[i] -= 1
                f1[j] += 1
                f2[j] -= 1
                f2[i] += 1
                if compare(f1, f2):
                    return True
                # Balance back
                f1[i] += 1
                f1[j] -= 1
                f2[j] += 1
                f2[i] -= 1
        return False
