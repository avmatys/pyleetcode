from typing import List

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq = [False] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            if freq[idx]:
                return ch
            freq[idx] = True
        return None
