from typing import List

class Solution:
    def minNumberOfSeconds(self, h: int, times: List[int]) -> int:
        heap = [(t, t, 1) for t in times]
        heapq.heapify(heap)
        for _ in range(h - 1):
            total, wtime, x = heapq.heappop(heap)
            heapq.heappush(heap, (total + (wtime * (x + 1)), wtime, x + 1))
        return heapq.heappop(heap)[0]
