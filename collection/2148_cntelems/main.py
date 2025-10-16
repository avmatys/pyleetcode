from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        l, r = 0, n - 1
        if nums[l] == nums[r]:
            return 0
        return sum(nums[l] < x < nums[r] for x in nums)
