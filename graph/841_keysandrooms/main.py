from typing import List
from datetime import datetime
from typing import Optional
from collections import deque

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/keys-and-rooms/description/
class Solution:

    @timeit
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set([0])
        while queue:
            i = queue.popleft()
            for room in rooms[i]: 
                if room in visited:
                    continue
                queue.append(room)
                visited.add(room)
        return len(visited) == len(rooms)

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[1],[2],[3],[]], True)
    ]
    for case in cases:
        expected = case[1]
        result = solution.canVisitAllRooms(case[0])
        judge(result, expected)
    
   
