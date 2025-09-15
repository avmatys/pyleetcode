from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        self.res = float('inf')
        n = len(toppingCosts)

        def solve(idx, cost):
            if idx == n:
                if abs(cost - target) < abs(self.res - target):
                    self.res = cost
                elif abs(cost - target) == abs(self.res - target) and cost < self.res:
                    self.res = cost
                return
            # Skip current topping
            solve(idx + 1, cost)
            # Add 1 current topping
            solve(idx + 1, cost + toppingCosts[idx])
            # Add 2 current toppings
            solve(idx + 1, cost + 2 * toppingCosts[idx])

        for bcost in baseCosts:
            solve(0, bcost)

        return self.res
