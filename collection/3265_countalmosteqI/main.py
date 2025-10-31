from typing import List

class Solution:

    def aeq(self, n1, n2):
        s1, s2 = str(n1), str(n2)
        n1, n2 = len(s1), len(s2)
        if n1 < n2:
            s2, s1 = s1, s2
            n2, n1 = n1, n2
        s2 = "0" * (n1 - n2) + s2
        f1, f2 = [0] * 10, [0] * 10
        for i in range(n1):
            f1[int(s1[i])] += 1
            f2[int(s2[i])] += 1
        for i in range(10):
            if f1[i] != f2[i]:
                return False
        return sum(int(s1[i] != s2[i]) for i in range(n1)) <= 2

    def countPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(1, n):
            for j in range(i):
                res += int(nums[i] == nums[j] or self.aeq(nums[i], nums[j]))
        return res
