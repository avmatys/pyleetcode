from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        chars = defaultdict(list)
        for i, ch in enumerate(s):
            chars[ch].append(i)
        for w in words:
            wcnt = len(w)
            prev_idx = -1
            for wch in w:
                wi = bisect.bisect_left(chars[wch], prev_idx + 1)
                if wi >= len(chars[wch]):
                    continue
                prev_idx = chars[wch][wi]
                wcnt -= 1
            if wcnt == 0:
                res += 1
        return res

