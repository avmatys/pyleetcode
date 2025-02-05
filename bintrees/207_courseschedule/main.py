from typing import List
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

# https://leetcode.com/problems/course-schedule/
class Solution:

    def __init__(self):
        self.nodes = dict()

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [ [] for _ in range(numCourses)]
        degree = [0] * numCourses
        # Adj list and set num of incoming edges 
        for j, i in prerequisites:
            graph[i].append(j)
            degree[j] += 1
        # Find all nodes without incoming edges
        nodes = [i for i in range(numCourses) if degree[i] == 0]
        for i in nodes:
            # Exclude edges from incoming
            for j in graph[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    nodes.append(j)
        return len(nodes) == numCourses


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    visited = dict()

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((2, [[1,0]]), True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        result = solution.canFinish(*input)
        judge(result, expected)

    
   