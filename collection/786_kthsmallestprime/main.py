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

# https://leetcode.com/problems/k-th-smallest-prime-fraction/description
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        for i in range(n - 1):
            heap.append((arr[i]/arr[-1], i, n - 1))
        heapq.heapify(heap)
        res = [-1, -1]
        for _ in range(k):
            _, i, j = heapq.heappop(heap)
            if i < j - 1:
                heapq.heappush(heap, (arr[i]/arr[j-1], i, j - 1))
            res = [arr[i], arr[j]]
        return res

