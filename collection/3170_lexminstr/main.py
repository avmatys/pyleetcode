from typing import List

class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        heap = []
        removed = [False] * n
        for i, ch in enumerate(s):
            if ch != '*':
                heapq.heappush(heap, (ord(ch), -i))
            else:
                _, j = heapq.heappop(heap)
                removed[-j] = True
                removed[i] = True
        res = []
        for i, ch in enumerate(s):
            if not removed[i]:
                res.append(ch)
        return "".join(res)


