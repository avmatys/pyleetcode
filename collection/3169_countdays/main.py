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

# https://leetcode.com/problems/count-days-without-meetings/description/
class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        days_with_meeting = 0
        n = len(meetings)
        i = 0

        while i < n:
            current_start = meetings[i][0]
            max_end = meetings[i][1]

            while i + 1 < n and max_end >= meetings[i + 1][0]:
                max_end = max(max_end, meetings[i + 1][1])
                i += 1

            days_in_interval = max_end - current_start + 1
            days_with_meeting += days_in_interval
            i += 1

        return days - days_with_meeting


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((10, [[5,7],[1,3],[9,10]]), 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.countDays(*input), expected)

    
   
