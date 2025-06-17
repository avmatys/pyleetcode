from typing import List

class Solution:

    count = 0
    diff = 0

    def divide(self, nums):
        n = len(nums)
        if n < 2:
            return nums
        mid = n // 2
        left_nums = self.divide(nums[:mid])
        right_nums = self.divide(nums[mid:])
        return self.merge(left_nums, right_nums)

    def merge(self, left, right):
        nl, nr = len(left), len(right)
        l, r = 0, 0
        # Count pairs
        while l < nl and r < nr:
            if left[l] <= right[r] + self.diff:
                self.count += nr - r
                l += 1
            else:
                r += 1
        # Merge 
        result = []
        l, r = 0, 0
        while l < nl and r < nr:
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        while l < nl:
            result.append(left[l])
            l += 1
        while r < nr:
            result.append(right[r])
            r += 1
        return result
            

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.diff = diff
        n = len(nums1)
        for i in range(n):
            nums1[i] -= nums2[i]
        self.divide(nums1)
        return self.count

        
        
