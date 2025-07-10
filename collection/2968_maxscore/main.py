from typing import List

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        csum = 0
        res = 0
        i = 0
        for j in range(n):
            csum += nums[j] - nums[(i + j) // 2]
            while csum > k:
                csum -= nums[(i + j + 1) // 2] - nums[i]
                i += 1
            res = max(res, j - i + 1)
        return res
