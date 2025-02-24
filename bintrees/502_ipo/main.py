from typing import List
from datetime import datetime
from typing import Optional
import heapq

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/ipo/description/
class Solution:
    @timeit
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_queue = [(capital[i], profits[i]) for i in range(len(capital))]
        heapq.heapify(capital_queue)
        total_profit = w
        profit_queue = []
        for _ in range(k):
            # Get list of the projects, which we can possibly start
            while capital_queue and capital_queue[0][0] <= total_profit:
                _, profit = heapq.heappop(capital_queue)
                heapq.heappush(profit_queue, -1 * profit)
            # Check if we can run at least one project
            if len(profit_queue) == 0:
                break
            # Select project with the biggest profit
            max_profit = -1 * heapq.heappop(profit_queue)
            total_profit += max_profit
        return total_profit    


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((2, 0, [1,2,3], [0,1,1]), 4),
        ((1, 2, [1,2,3], [0,1,2]), 5),
        ((2, 2, [1,2,3], [100,50,4]), 2),
        ((0, 2, [1,2,3], [1,0,0]), 2),
        ((2, 2, [9,2,3], [1,1,0]), 14),
        ((3, 0, [1,2,3], [0,1,2]), 6)
    ]
    for case in cases:
        result = solution.findMaximizedCapital(*case[0])
        judge(result, case[1])