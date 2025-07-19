from typing import List

class Solution:

    def calc(self, nums, q, k):
        n = len(nums)
        diff = [0] * (n + 1)
        for i in range(k):
            l, r, v = q[i]
            diff[l] += v
            diff[r+1] -= v
        curr = 0
        for i in range(n):
            curr += diff[i]
            if nums[i] > curr:
                return False
        return True

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
    
        l, r = 0, len(queries)
        if not self.calc(nums, queries, r):
            return -1

        while l < r:
            m = l + (r - l) // 2
            if self.calc(nums, queries, m):
                r = m
            else:
                l = m + 1
        return l
