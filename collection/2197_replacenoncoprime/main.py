from typing import List

class Solution:

    def gcd(self, a, b):
        if b == 0: return a
        else: return self.gcd(b, a % b)

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums)):
            num = nums[i]
            while stack and self.gcd(stack[-1], num) > 1:
                last = stack.pop()
                num = num * last // self.gcd(last, num)
            stack.append(num)
        return stack

