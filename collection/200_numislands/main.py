from typing import List
from datetime import datetime
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


# https://leetcode.com/problems/number-of-islands/description/
class Solution:

    @timeit
    # Solved using greedy approach as groups can be divided by N symbols
    def numIslands(self, grid: List[List[str]]) -> int:

        row_number = len(grid)
        column_number = len(grid[0])
        visited = [[0 for _ in range(column_number)] for _ in range(row_number)]

        def bfs(vertex):

            DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            vertexes_to_visit = deque()
            vertexes_to_visit.append(vertex)

            while len(vertexes_to_visit) > 0:
                # Get vertex
                current_vertex = vertexes_to_visit.popleft()
                # Calculate all possible 4 direction
                for direction in DIRECTIONS:
                    next_vertex = (current_vertex[0] + direction[0], current_vertex[1] + direction[1])
                    # Check if we are in the grid
                    if 0 <= next_vertex[0] < row_number and 0 <= next_vertex[1] < column_number:
                        # Point was not visited yet
                        if visited[next_vertex[0]][next_vertex[1]] == 0:
                            # Check if next point is an island
                            if grid[next_vertex[0]][next_vertex[1]] == '1':
                                vertexes_to_visit.append(next_vertex)
                            # Mark as visited
                            visited[next_vertex[0]][next_vertex[1]] = 1

        # Start grid processing
        num_islands = 0
        for i in range(row_number):
            for j in range(column_number):
                # Current vertex was not visited yet
                if visited[i][j] == 0:
                    # Mark as visited
                    visited[i][j] = 1
                    # This is an island
                    if grid[i][j] == '1':
                        num_islands += 1
                        bfs((i,j))
                    

        return num_islands
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [([["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]], 1),
             ([["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]], 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.numIslands(input), expected)

    
   