from typing import List
from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/paint-house-iii/
# houses = info about house color. If houses[i] != 0 -> house shouldn't be painted
# cost = cost of pait i-th house to j+1 color
# m = number of houses
# n = number of colors
# target = number of groups of neighborhoods
class Solution:

    @timeit
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
       
        # Cache is used to store min cost for steps
        cached_costs = {}

        def dfs (i, target, prev_color):
           
            key = (i, target, prev_color)

            # Reached to the end
            # Cost is zero if we succesfully found needed count of targets
            # Cist is INF if we found too many targets
            if i == len(houses) or target < 0:
                return 0 if target == 0 else float('inf')
            
            if key not in cached_costs:
                # We should paint house once again
                if houses[i] == 0:
                    # Let's try to paint using all availalble colors
                    # If color is equal to the prev one - doesn't decrement target count
                    # If color is not equal - decrement as we create a new group 
                    min_cost = float('inf')
                    for new_color in range(1, n+1):
                        decrement_value = prev_color != new_color
                        # Start calc from beggining to the end
                        calc_cost = dfs(i+1, target - decrement_value, new_color) + cost[i][new_color-1]
                        if calc_cost < min_cost:
                            min_cost = calc_cost
                    cached_costs[key] = min_cost
                # House was painted last year
                else:
                    decrement_value = prev_color != houses[i]
                    calc_cost = dfs(i+1, target - decrement_value, houses[i])
                    cached_costs[key] = calc_cost

            # Return calculated value   
            return cached_costs[key]

        min_cost = dfs(0, target, -1)

        return min_cost if min_cost != float('inf') else -1

    
if __name__ == '__main__':
    solution = Solution()    
    assert 9 == solution.minCost([0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3)
    assert 11 == solution.minCost([0,2,1,2,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3)
    assert -1 == solution.minCost([3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3)