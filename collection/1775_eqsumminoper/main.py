from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s2 > s1:
            s1, s2 = s2, s1
            nums1, nums2 = nums2, nums1
        # s1 should be decreased x - 1
        # s2 should be increased 6 - x
        diff = s1 - s2
        delta = [x - 1 for x in nums1] + [6 - x for x in nums2]
        for i, x in enumerate(sorted(delta, reverse=True)):
            diff -= x
            if diff <= 0:
                return i + 1
        return -1
