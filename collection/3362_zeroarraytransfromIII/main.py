from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        m, n = len(queries), len(nums)
        prefix = [0] * (n + 1)
        queries.sort()
        heap = []
        curr = 0
        qi = 0
        for i in range(n):
            # Add new available queries
            while qi < m and queries[qi][0] <= i:
                heapq.heappush(heap, -queries[qi][1])
                qi += 1
            # Calculate current possible diff
            curr += prefix[i]
            # Check if we need some new queries
            while nums[i] > curr:
                # Don't have a proper query to extend
                if not heap or -heap[0] < i:
                    return -1
                # Extend the range
                curr += 1
                idx = -heapq.heappop(heap)
                prefix[idx + 1] += -1
        return len(heap)

