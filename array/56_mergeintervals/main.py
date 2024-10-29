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


# https://leetcode.com/problems/merge-intervals/description/
class Solution:

    @timeit
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)

        result = []
        for interval in sorted_intervals:
            if len(result) == 0:
                result.append(interval)
            else:
                latest_interval = result.pop()
                if interval[0] <= latest_interval[1]:
                    latest_interval[1] = interval[1] if interval[1] > latest_interval[1] else latest_interval[1] 
                    result.append(latest_interval)
                else:
                    result.append(latest_interval)
                    result.append(interval)
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([[1,3],[8,10],[2,6],[15,18]]), [[1,6],[8,10],[15,18]]),
        (([[1,4],[4,5]]), [[1,5]]),
        (([[1,4],[2,3]]), [[1,4]])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.merge(input), expected)


    
   