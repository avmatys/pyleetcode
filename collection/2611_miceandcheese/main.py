from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        heap = [(reward2[i] - r, i) for i, r in enumerate(reward1)]
        heapq.heapify(heap)
        sum1 = 0
        sum2 = sum(reward2)
        for _ in range(k):
            _, i = heapq.heappop(heap)
            sum1 += reward1[i]
            sum2 -= reward2[i]
        return sum1 + sum2
