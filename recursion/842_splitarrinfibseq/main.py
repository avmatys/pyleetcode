from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:

        n = len(num)
        MAX_INT = 2**31 - 1

        def helper(start, seq):
            if start == n:
                return len(seq) > 2
            for end in range(start + 1, n + 1):
                value = int(num[start:end])
                if num[start] == '0' and end - start > 1 or value > MAX_INT:
                    break
                expected = value if len(seq) < 2 else seq[-2] + seq[-1]
                if value > expected:
                    break
                elif value == expected:
                    seq.append(value)
                    if helper(end, seq):
                        return True
                    seq.pop()
            return False

        seq = []
        helper(0, seq)
        return seq
