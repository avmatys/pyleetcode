from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        n = len(arr1)
        m = len(arr2)
        arr2.sort()
        dp = { }

        def dfs(i, prev):
            if i == n:
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]
            cost = float('inf')
            if arr1[i] > prev:
                # Skip current and go to the next
                cost = dfs(i + 1, arr1[i])
            ni = bisect.bisect_right(arr2, prev)
            if ni < m:
                # We change an item
                cost = min(cost, 1 + dfs(i + 1, arr2[ni]))
            dp[(i, prev)] = cost
            return cost

        res = dfs(0, -1)
        return res if res < float('inf') else -1

