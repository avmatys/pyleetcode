from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        res = 0
        point = 0
        tank = startFuel
        while tank < target:
            while point < len(stations) and stations[point][0] <= tank:
                heapq.heappush(heap, -stations[point][1])
                point += 1
            if not heap:
                return -1
            tank -= heapq.heappop(heap)
            res += 1
        return res
