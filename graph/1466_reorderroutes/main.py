from typing import List
from datetime import datetime
from typing import Optional
from collections import deque, defaultdict

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
class Solution:

    def count_changes(self, adj_list, visited, frm):
        visited[frm] = True
        count = 0
        for to in adj_list[frm]:
            if not visited[abs(to)]:
                count += self.count_changes(adj_list, visited, abs(to)) + (to > 0)
        return count

    @timeit
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for start, end in connections:
            adj_list[start].append(end)
            adj_list[end].append(-start)
        visited = [False] * n
        return self.count_changes(adj_list, visited, 0)

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((6, [[0,1],[1,3],[2,3],[4,0],[4,5]]), 3)
    ]
    for case in cases:
        expected = case[1]
        result = solution.minReorder(*case[0])
        judge(result, expected)
    
   
