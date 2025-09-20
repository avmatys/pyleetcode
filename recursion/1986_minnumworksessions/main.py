from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:

        n = len(tasks)
        tasks.sort(reverse=True)

        @lru_cache(None)
        def helper(used, time):
            if used == (1 << n) - 1:
                return 0
            res = float('inf')
            for i, t in enumerate(tasks):
                if used & (1 << i): 
                    continue
                if time >= t:
                    res = min(res, helper(used | (1 << i), time - t))
                else:
                    res = min(res, 1 + helper(used | (1 << i), sessionTime - t))
            return res
        
       
        return helper(0, 0)
