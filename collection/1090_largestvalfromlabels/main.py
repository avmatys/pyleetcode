from typing import List

class Solution:
   
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
        used = defaultdict(int)
        heap = []
        for l, v in zip(labels, values):
            heapq.heappush(heap, (-v, l))
        
        res = 0
        while heap and numWanted > 0:
            v, l = heapq.heappop(heap)
            if used[l] < useLimit:
                used[l] += 1
                res -= v
                numWanted -= 1
       
        return res
