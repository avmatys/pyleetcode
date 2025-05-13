from typing import List
from datetime import datetime


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m = len(matrix)
        for i in range(m):
            heap.append((matrix[i][0], i, 0))
        heapq.heapify(heap)
        for _ in range(k):
            num, row, col = heapq.heappop(heap)
            if col < m - 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        return num
