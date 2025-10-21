from typing import List

class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = [0] * 10
        for ch in num:
            freq[int(ch)] += 1
        # One digit 
        if all(x <= 1 for x in freq[1:]):
            return str(max(i for i in range(10) if freq[i] > 0))
        result = []
        # Symmetric
        for i in range(9, -1, -1):
            k = freq[i] // 2
            result.append(str(i) * k)
            freq[i] -= k * 2
        # Mid
        mid = -1
        for i in range(9, -1, -1):
            if freq[i] > 0:
                mid = i
                break
        # Form result
        return "".join(result) + (str(mid) if mid >= 0 else "") + "".join(reversed(result))
