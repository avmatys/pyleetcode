from typing import List
from datetime import datetime


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/gas-station/description/
class Solution:

    @timeit
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        totalCost = 0
        totalGas = 0
        tank = 0
        station = 0

        for i in range(len(gas)):
            totalCost += cost[i]
            totalGas += gas[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                station = i + 1
        
        if totalGas >= totalCost:
            return station
        
        return -1


def judge(result, expected):
   assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,2,3,4,5], [3,4,5,1,2]), 3),
        (([2,3,4], [3,4,3]), -1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.canCompleteCircuit(*input), expected)


    
   