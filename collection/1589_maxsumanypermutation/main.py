from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)
        for l, r in requests:
            freq[l] += 1
            freq[r + 1] -= 1
        for i in range(1, n + 1):
            freq[i] += freq[i-1]
        res = 0
        for x, f in zip(sorted(nums), sorted(freq[:n])):
            res += x * f
        return res % (10**9 + 7)
