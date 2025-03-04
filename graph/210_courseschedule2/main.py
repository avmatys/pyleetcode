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

# https://leetcode.com/problems/course-schedule-ii/
class Solution:

    def __init__(self):
        self.nodes = dict()

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [ [] for _ in range(numCourses)]
        degree = [0] * numCourses
        # Adj list and set num of incoming edges 
        for j, i in prerequisites:
            graph[i].append(j)
            degree[j] += 1
        # Find all nodes without incoming edges
        nodes = [i for i in range(numCourses) if degree[i] == 0]
        result = []
        for i in nodes:
            # Exclude edges from incoming
            result.append(i)
            for j in graph[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    nodes.append(j)
        return result if len(nodes) == numCourses else []


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    visited = dict()

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ((2, [[1,0]]), [0,1]),
        ((4, [[1,0],[2,0],[3,1],[3,2]]), [0,2,1,3])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        result = solution.findOrder(*input)
        judge(result, expected)

    
   