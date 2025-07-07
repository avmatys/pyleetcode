from typing import List

class Solution:

    def count_flips(self, nums, groups, k):
        if k == 1:
            res = sum(x == i % 2 for i, x in enumerate(nums))
            return min(res, len(nums) - res)
        else:
            return sum(group // (k + 1) for group in groups)
        
    def minLength(self, s: str, numOps: int) -> int:

        # Convert char to int
        nums = list(map(int, s))
        n = len(nums)

        # Split nums in the groups
        groups = []
        clen = 1
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                clen += 1
            else:
                groups.append(clen)
                clen = 1
        groups.append(clen)

        # Start bin search
        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            needed = self.count_flips(nums, groups, m)
            if needed <= numOps:
                r = m
            else:
                l = m + 1
        return l
    

        
