from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        right = [0] * n
        freq = defaultdict(int)
        for i in range(n - 1, -1, -1):
            right[i] = freq[nums[i] * 2]
            freq[nums[i]] += 1
        freq.clear()
        res = 0
        for i in range(n):
            res += freq[nums[i] * 2] * right[i]
            freq[nums[i]] += 1
        return res % (10**9 + 7)
