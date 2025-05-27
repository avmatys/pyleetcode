from typing import List

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        heap = []
        n = len(nums1)
        res = [-1] * n
        csum = 0
        nums = []
        combined = [(n1, n2, i) for i, (n1, n2) in enumerate(zip(nums1, nums2))]
        combined.sort(key = lambda x: x[0])
        for i, (n1, n2, j) in enumerate(combined):
            # Repeated number
            if i > 0 and combined[i-1][0] == n1:
                res[j] = res[combined[i-1][2]]
            else:
                res[j] = csum
            heapq.heappush(heap, n2)
            csum += n2
            if len(heap) > k:
                csum -= heapq.heappop(heap)
        return res
