from typing import List, Dict
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


# https://leetcode.com/problems/evaluate-division
class Solution:

    @timeit
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build_graph(equations, values)
        result = []
        for query in queries:
            result.append(self.calc_weight(query[0], query[1], graph, set()))
        return result

    def build_graph(self, equations: List[List[str]], values: List[float]) -> List[float]:
        graph = dict()
        for i, eq in enumerate(equations):
            start = eq[0]
            end = eq[1]
            if start not in graph:
                graph[start] = dict()
                graph[start][start] = 1.0
            if end not in graph:
                graph[end] = dict()
                graph[end][end] = 1.0
            if end not in graph[start]:
                graph[start][end] = values[i]
            if start not in graph[end]:
                graph[end][start] = 1 / values[i]
        return graph
    
    def calc_weight(self, start: str, end: str, graph: Dict, visited):
        if start not in graph:
            return -1.0
        if end in graph[start]:
            return graph[start][end]
        visited.add(start)
        for n_key, n_weight in graph[start].items():
            if n_key in visited:
                continue
            weight = self.calc_weight(n_key, end, graph, visited)
            if weight != -1.0:
                return n_weight * weight
        
        return -1.0


    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert len(result) == len(expected)
    for i in range(len(result)):
        assert result[i] == expected[i]


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]), [6.00000,0.50000,-1.00000,1.00000,-1.00000])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        result = solution.calcEquation(*input)
        judge(result, expected)

    
   