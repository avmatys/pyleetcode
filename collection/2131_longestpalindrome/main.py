from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        res = 0
        odd = 0
        for s, v in cnt.items():
            r = s[::-1]
            if s == r:
                res += 2 * 2 * (v // 2)
                odd |= v & 1
            elif cnt[r] > 0:
                res += 2 * 2 * min(cnt[s], cnt[r])
            cnt[s] = 0
        res += 2 if odd & 1 else 0   
        return res 
