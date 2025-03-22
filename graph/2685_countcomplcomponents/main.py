from typing import List, Set
from datetime import datetime
from typing import Optional

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/count-the-number-of-complete-components/description/
class Solution:
    def dfs(self, adj_list, node, visited, meta):
        if visited[node]:
            return
        meta[0], meta[1] = meta[0] + 1, meta[1] + len(adj_list[node])
        visited[node] = True
        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                self.dfs(adj_list, neighbour, visited, meta)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = [False] * n
        count = 0
        for node in range(n):
            if not visited[node]:
                meta = [0,0] # 0 = nodes count * 2, 1 = edges count
                self.dfs(adj_list, node, visited, meta)
                if (meta[0] * (meta[0] - 1)) / 2 == meta[1] / 2:
                    count += 1
        return count



def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    cases = [
        ((6, [[0,1],[0,2],[1,2],[3,4]]), 3),
        ((6, [[0,1],[0,2],[1,2],[3,4],[3,5]]), 1)
    ]
    for case in cases:
        solution = Solution()
        result = solution.countCompleteComponents(*case[0])
        judge(result, case[1])
