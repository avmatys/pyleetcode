from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heap.append((math.sqrt(x * x + y * y), [x,y]))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        
