from typing import List

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        count = [0] * 2001
        tasks.sort(key=lambda x: x[1])
        for st, end, d in tasks:
            d -= sum(count[st:end+1])
            while d > 0:
                d -= 1 if count[end] == 0 else 0
                count[end] = 1
                end -= 1
        return sum(count)



