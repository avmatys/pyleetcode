from typing import List

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7
        inventory.sort()
        n = len(inventory)
        ci = n - 1
        cx = inventory[ci]
        res = 0
        while orders > 0:
            while ci >= 0 and inventory[ci] == cx:
                ci -= 1
            # Set current value
            x = inventory[ci] if ci >= 0 else 0
            # Calc number of the same colors
            colors = n - 1 - ci
            # Calc number of items to buy
            buy = (cx - x) * colors
            # Check if we can buy all of them
            if buy <= orders:
                res += colors * ((cx + x + 1) * (cx - x)) // 2
            # We can buy partially
            else:
                full = orders // colors
                part = orders % colors
                res += colors * ((cx + (cx - full) + 1) * full) // 2
                res += (cx - full) * part
            orders -= buy
            res %= MOD
            cx = x
        return res

