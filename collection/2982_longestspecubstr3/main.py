from typing import List

class Solution:
    def maximumLength(self, s: str) -> int:
        # Group elements
        n = len(s)
        lens = [1] * n
        for i in range(1, n):
            if s[i] == s[i-1]:
                lens[i] = lens[i-1] + 1
        # Add groups to the heaps - up to 3
        heaps = [[] for i in range(26)]
        for ch, l in zip(s, lens):
            idx = ord(ch) - ord('a')
            heapq.heappush(heaps[idx], l)
            if len(heaps[idx]) > 3:
                heapq.heappop(heaps[idx]) # Mantain max
        # Find max among the heaps
        res = -1
        for i in range(26):
            if len(heaps[i]) < 3: continue
            res = max(res, heaps[i][0])
        return res
