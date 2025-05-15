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

# https://leetcode.com/problems/maximum-number-of-eaten-apples/description/
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        heap = []
        res = 0
        i = 0
        while i < n or heap:
            # Add new apples
            if i < n and apples[i] > 0:
                heapq.heappush(heap, (i + days[i], apples[i]))
            # Remove old apples
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            # Eat apples
            if heap:
                res += 1
                day, cnt = heapq.heappop(heap)
                if cnt > 1:
                    heapq.heappush(heap, (day, cnt - 1))
            i += 1
        return res
