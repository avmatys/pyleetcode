from typing import List

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m, n = len(matrix), len(matrix[0])
        prev = [0] * (n + 1)
        for i in range(m):
            curr = [0]
            for j in range(n):
                curr.append(matrix[i][j] ^ curr[j] ^ prev[j] ^ prev[j + 1])
                heapq.heappush(heap, curr[j + 1])
                if len(heap) > k:
                    heapq.heappop(heap)
            prev = curr
        return heap[0]
