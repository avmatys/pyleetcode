from typing import List

class Solution:
    def lastRemaining(self, n: int) -> int:

        head = 1
        step = 1
        remaining = n
        dir_left = True

        while remaining > 1:
            if dir_left or remaining % 2 == 1:
                head += step
            step *= 2
            remaining //= 2
            dir_left = not dir_left

        return head

