from typing import List

class Solution:

    """
    101
    110
    """
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suff = [0] * n
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] | nums[i + 1]
        res = 0
        pref = 0
        for i in range(n):
            curr = suff[i] | (nums[i] << k) | pref
            res = max(res, curr)
            pref |= nums[i]
        return res 

        
        
