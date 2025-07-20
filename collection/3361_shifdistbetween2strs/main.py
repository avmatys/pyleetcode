from typing import List

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], prevCost: List[int]) -> int:
        next_prefix = [0] * 27
        prev_prefix = [0] * 27
        for i in range(1, 27):
            next_prefix[i] = next_prefix[i - 1] + nextCost[i - 1]
            prev_prefix[26 - i] = prev_prefix[26 - i + 1] + prevCost[26 - i]
        res = 0
        for sch, tch in zip(s, t):
            src_code = ord(sch) - ord('a')
            tgt_code = ord(tch) - ord('a')
            if src_code == tgt_code:
                continue
            if tgt_code > src_code:
                fwd_cost = next_prefix[tgt_code] - next_prefix[src_code]
                bwd_cost = prev_prefix[0] - prev_prefix[src_code + 1] + prev_prefix[tgt_code + 1]
            else:
                fwd_cost = next_prefix[26] - next_prefix[src_code] + next_prefix[tgt_code]
                bwd_cost = prev_prefix[tgt_code + 1] - prev_prefix[src_code + 1]
            res += min(fwd_cost, bwd_cost)
        return res
