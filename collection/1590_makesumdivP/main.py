from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        rest = sum(nums) % p
        rmap = {0: -1}
        curr = 0
        res = n
        for i, x in enumerate(nums):
            curr = (curr + x) % p
            rmap[curr] = i
            need = (curr - rest + p) % p
            if need in rmap:
                res = min(res, i - rmap[need])
        return -1 if res == n else res
