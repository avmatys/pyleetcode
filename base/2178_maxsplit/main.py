from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        res = []
        x = 2
        while finalSum > 0:
            if finalSum == x or finalSum > 2 * x:
                res.append(x)
                finalSum -= x
            x += 2
        return res

