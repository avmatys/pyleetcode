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


# https://leetcode.com/problems/insert-interval
class Solution:

    @timeit
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new_start, new_end = newInterval
        idx = 0
        n = len(intervals)
        result_list = []

        # Copy all intervals, which are before new start
        while idx < n and intervals[idx][0] < new_start:
            result_list.append(intervals[idx])
            idx += 1

        # Add new interval and merge if needed
        if len(result_list) == 0 or result_list[-1][1] < new_start:
            result_list.append(newInterval)
        else:
            result_list[-1][1] = max(result_list[-1][1], new_end)

        # Add remaining interval with merge if needed
        for i in range(idx, n):
            curr_start, curr_end = intervals[i]
            if result_list[-1][1] < curr_start:
                result_list.append(intervals[i])
            else:
                result_list[-1][1] = max(result_list[-1][1], curr_end)

        return result_list



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    for arr in result:
        assert arr in  expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([[1,3],[6,9]], [2,5]), [[1,5],[6,9]]),
        (([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.insert(*input), expected)


    
   