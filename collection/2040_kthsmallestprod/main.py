from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def prod_count(x1, value):
            res = 0
            if x1 > 0:
                res = bisect.bisect_right(nums2, math.floor(value / x1))
            elif x1 < 0:
                res = len(nums2) - bisect.bisect_left(nums2, math.ceil(value / x1))
            elif value >= 0:
                res = len(nums2)
            return res

        n1 = len(nums1)
        l = -(10**10)
        r = 10**10
        while l < r:
            m = l + (r - l) // 2
            count = 0
            for x1 in nums1:
                count += prod_count(x1, m)
            if count < k:
                l = m + 1
            else:
                r = m
        return l


