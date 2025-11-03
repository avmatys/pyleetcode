from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0: return False
        freq = Counter(nums)
        g = n // k
        for v in freq.values():
            if v > g: return False
        return True
