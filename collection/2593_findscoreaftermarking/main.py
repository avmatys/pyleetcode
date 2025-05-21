from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = set()
        heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)
        res = 0
        while len(marked) < n:
            x, i = heapq.heappop(heap)
            if i not in marked:
                res += x
                marked.add(i)
                if i - 1 >= 0: marked.add(i - 1)
                if i + 1 < n : marked.add(i + 1)
        return res 
