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


# https://leetcode.com/problems/car-fleet/description/
class Solution:

    @timeit
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        speed_map = {position[i]: speed[i] for i in range(n)}
        sorted_pos = sorted(position, reverse=True)
        stack = []
        for pos in sorted_pos:
            time = (target - pos) / speed_map[pos]
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)
    
    @timeit
    def carFleet2(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - pos) / sp for pos, sp in sorted(zip(position, speed))]
        fleets = 0
        last_time = 0
        for curr_time in reversed(times):
            if curr_time > last_time:
                fleets += 1
                last_time = curr_time
        return fleets


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
             ((12, [10,8,0,5,3], [2,4,1,1,3]), 3),
             ((100, [10], [10]), 1),
             ((100, [0,2,4], [4,2,1]), 1),
             ((10, [0,4,2], [2,1,3]), 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.carFleet2(*input), expected)

    
   