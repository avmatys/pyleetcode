from typing import List

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        fl, fc = [0] * 101, [0] * 26
        for w in words:
            fl[len(w)] += 1
            for ch in w:
                fc[ord(ch) - ord('a')] += 1
        pairs = 0
        for i in range(26):
            pairs += fc[i] // 2
        res = fl[1]
        for i in range(2, 101):
            if fl[i] == 0 or pairs == 0: continue
            for _ in range(fl[i]):
                if pairs < i // 2:
                    break
                pairs -= i // 2
                res += 1
        return res
