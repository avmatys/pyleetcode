from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq = Counter(nums)
        nums.sort()
        nset = set()
        for x in nums:
            nset.add(x)
            nset.add(x - k)
            nset.add(x + k)
        res = 0
        for x in nset:
            l = bisect.bisect_left(nums, x - k)
            r = bisect.bisect_right(nums, x + k)
            operations = min(numOperations, r - l - freq[x])
            res = max(res, freq[x] + operations)
        return res
