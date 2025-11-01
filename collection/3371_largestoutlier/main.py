from typing import List

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        freq = Counter(nums)
        tsum = sum(nums)
        res  = float('-inf')
        # tsum = x (outlier) + esum (special sum) + sum(nums[n-2])
        for x in freq.keys():
            y = tsum - x
            if y & 1: # Sum should be even
                continue
            esum = y // 2 # Special sum element
            need = 1 + int(esum == x) # Min freq needed
            if freq[esum] < need:
                continue
            res = max(res, x)
        return res
