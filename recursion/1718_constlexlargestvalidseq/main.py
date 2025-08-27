from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # idx - place to insert
        # seq - curr sequence
        # used - arr of used nums
        def helper(idx, seq, used):
            # We reach out the end of the sequence
            if idx == len(seq):
                return True
            # Check if the current idx is set
            if seq[idx] != 0:
                return helper(idx+1, seq, used)
            # Iterate through numbers
            for x in range(n, 0, -1):
                if used[x]: continue
                used[x] = True
                seq[idx] = x
                # We should place only one
                if x == 1:
                    if helper(idx+1, seq, used):
                        return True
                elif idx + x < len(seq) and seq[idx+x] == 0:
                    seq[idx+x] = x
                    if helper(idx+1, seq, used):
                        return True
                    # Undo for backtracking
                    seq[idx+x] = 0
                # Undo placement of the number
                seq[idx] = 0
                used[x] = False
            return False

        used = [False] * (n+1)
        seq = [0] * (2*n-1)
        helper(0, seq, used)
        return seq

