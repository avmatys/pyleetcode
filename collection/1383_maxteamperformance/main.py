from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        csum = 0
        res = 0
        for e,s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(heap, s)
            csum += s
            if len(heap) > k:
                csum -= heapq.heappop(heap)
            res = max(res, csum * e)
        return res % (10**9 + 7)
        
