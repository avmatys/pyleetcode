from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        def two_top(start):
            cnt = [0] * 100001
            first, second = 0, 0
            for i in range(start, len(nums), 2):
                cnt[nums[i]] += 1
                if cnt[nums[i]] >= cnt[first]:
                    if nums[i] != first:
                        second = first
                    first = nums[i]
                elif cnt[nums[i]] > cnt[second]:
                    second = nums[i]
            return (first, cnt[first], cnt[second])

        n = len(nums)
        ex, ec1, ec2 = two_top(0)
        ox, oc1, oc2 = two_top(1)
        if ex != ox:
            return n - ec1 - oc1
        return min(n - ec1 - oc2, n - ec2 - oc1)
