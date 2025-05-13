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

# https://leetcode.com/problems/ugly-number-ii/description/
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        h2 : 6 8 10
        h3 : 6 9 12 15
        h5 : 10 12 15 25

        1 -> 2, 3, 5
        2 -> 4, 5, 6: 3,4,5,6
        3 -> 6, 9, 15: 4,5,6,9,15
        4 -> 8, 12, 20: 5,6,8,9,12,15,20
        5 -> 10, 15, 25

        """
        res = 1
        heap = [1]
        values = set()
        for _ in range(1,n):
            num = heap[0]
            while heap and heap[0] == num:
                heapq.heappop(heap)
            for i in (2,3,5):
                heapq.heappush(heap, num * i)
        return heap[0]
