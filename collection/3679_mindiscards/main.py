from typing import List

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        n = len(arrivals)
        freq = [0] * 100001
        res = 0
        for i in range(n):
            # Shrink a window
            if i >= w:
                freq[arrivals[i - w]] -= (arrivals[i-w] != 0)
            # Check if should discard
            if freq[arrivals[i]] == m:
                arrivals[i] = 0
                res += 1
            else:
                freq[arrivals[i]] += 1
        return res
