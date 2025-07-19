from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r+1] -= 1
        curr = 0
        for i in range(n):
            curr += diff[i]
            if nums[i] > curr:
                return False
        return True
