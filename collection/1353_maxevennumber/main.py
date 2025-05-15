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

# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        heap = []
        res = 0
        i = 0
        cday = -1
        while i < n or heap:
            # Init current day
            if not heap:
                cday = events[i][0]
            # Add available events
            while i < n and events[i][0] <= cday:
                heapq.heappush(heap, events[i][1])
                i += 1
            # We can process one event today
            if heap:
                res += 1
                heapq.heappop(heap)
            cday += 1
            # Remove old events
            while heap and heap[0] < cday:
                heapq.heappop(heap)
        return res

