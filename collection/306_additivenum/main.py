from typing import List

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        # Generate all possible combinations
        for i, j in itertools.combinations(range(1, n//3 * 2 + 1), 2):
            prev1, prev2 = num[:i], num[i:j]
            # Check that num without leading zeroes
            if prev1 != str(int(prev1)) or prev2 != str(int(prev2)):
                continue
            # Check chain
            while j < n:
                expected = str(int(prev1) + int(prev2))
                if not num.startswith(expected, j):
                    break
                j += len(expected)
                prev1 = prev2
                prev2 = expected
            if j == n:
                return True
        return False



