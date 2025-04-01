from typing import List
from datetime import datetime
from collections import defaultdict

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/jump-game-iv/description/
class Solution:
    def bfs(self, graph, arr, n):
        queue = [0]
        visited = {0}
        levels = 0
        while queue:
            next_queue = []
            for idx in queue:
                if idx == n - 1:
                    return levels
                # Process the same values
                for next_idx in graph[arr[idx]]:
                    if next_idx not in visited:
                        next_queue.append(next_idx)
                        visited.add(next_idx)
                # Process node to the left and right
                for next_idx in [idx - 1, idx + 1]:
                    if 0 <= next_idx < n and next_idx not in visited:
                        next_queue.append(next_idx)
                        visited.add(next_idx)
                graph[arr[idx]].clear()
            queue = next_queue
            levels += 1
        return -1

    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        graph = defaultdict(list)
        for i in range(n):
            graph[arr[i]].append(i)
        return self.bfs(graph, arr, n)
        

def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([100,-23,-23,404,100,23,23,23,3,404], 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minJumps(input), expected)

    
   
