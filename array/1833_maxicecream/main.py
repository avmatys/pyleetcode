from typing import List
from datetime import datetime
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


# https://leetcode.com/problems/maximum-ice-cream-bars/description
class Solution:

    @timeit
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        def count_sort(nums: List[int]):
            # Find max value
            max_value = max(nums)
            # Allocate memory to calc number of items
            nums_count = [0] * (max_value + 1)
            for num in nums:
                nums_count[num] += 1
            # Culmulate sum
            for i in range(1, len(nums_count)):
                nums_count[i] += nums_count[i-1]
            # Find position in the result array
            result = [0] * len(nums)
            for i in range(len(nums) - 1, -1, -1):
                result[nums_count[nums[i]] - 1] = nums[i]
                nums_count[nums[i]] -= 1
            return result

        sorter_costs = count_sort(costs)
        print(sorter_costs)
        total_count = 0
        for cost in sorter_costs:
            if cost <= coins:
                coins -= cost
                total_count += 1
            else:
                break

        return total_count
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,3,2,4,1], 7), 4),
        (([10,6,8,7,7,8], 5), 0)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxIceCream(*input), expected)


    
   