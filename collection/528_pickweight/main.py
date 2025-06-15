from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = w[:]
        for i in range(1, len(self.prefix)):
            self.prefix[i] += self.prefix[i-1]

    def pickIndex(self) -> int:
        return bisect.bisect(self.prefix, random.randint(0, self.prefix[-1] - 1))
