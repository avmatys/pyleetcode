from typing import List

class Solution:

    def isKthRepeated(self, orig, pattern, start, k):
        if k == 0:
            return True
        n, m, j = len(orig), len(pattern), 0
        for i in range(start, n):
            if orig[i] == pattern[j]:
                j += 1
            if j == m:
                return self.isKthRepeated(orig, pattern, i + 1, k - 1)
        return False


    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        chars = [chr(i + ord('a')) for i in range(25, -1, -1) if freq[i] >= k]
        substrings = deque(chars)
        res = ""
        while substrings:
            curr = substrings.popleft()
            if len(curr) > len(res):
                res = curr
            for ch in chars:
                nxt = curr + ch
                if self.isKthRepeated(s, nxt, 0, k):
                    substrings.append(nxt)
        return res
