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

# Definition for a graph
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(adj_list):
    if len(adj_list) == 0:
        return None
    nodes  = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    return nodes[0] 

# https://leetcode.com/problems/clone-graph/
class Solution:

    def __init__(self):
        self.nodes = dict()

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        if node in self.nodes:
            return self.nodes[node]
        
        new_node = Node(node.val)
        self.nodes[node] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neighbor))

        return new_node        


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    visited = dict()
    def compare_graphs(node_1, node_2):
        if node_1 is None and node_2 is None:
            return True
        if node_1 is None or node_1 is None:
            return False
        if node_1 in visited:
            if node_2 in visited[node_1]:
                return True 
            else:
                visited[node_1].add(node_2)
        else:
            visited[node_1] = set([node_2])
        if node_1.val != node_2.val:
            return False
        if len(node_1.neighbors) != len(node_2.neighbors):
            return False
        for i in range(len(node_1.neighbors)):
            if not compare_graphs(node_1.neighbors[i], node_2.neighbors[i]):
                return False
        return True
    assert compare_graphs(result, expected)     


if __name__ == '__main__':
    solution = Solution()
    cases = [
        [[2,4],[1,3],[2,4],[1,3]],
        []
    ]
    for case in cases:
        input = build_graph(case)
        expected = input
        result = solution.cloneGraph(input)
        judge(result, expected)

    
   