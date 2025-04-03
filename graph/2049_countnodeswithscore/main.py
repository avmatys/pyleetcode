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

# https://leetcode.com/problems/count-nodes-with-the-highest-score/description/
class Solution:
    def calc_subtrees(self, adj_list, n, node, subtrees):
        if node > n - 1:
            return None
        size = 1
        for child in adj_list[node]:
            if child not in subtrees:
                self.calc_subtrees(adj_list, n, child, subtrees)
            size += subtrees[child]
        subtrees[node] = size

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # Build adj list
        total = len(parents)
        adj_list = [[] for _ in range(total)]
        for i in range(1, total):
            adj_list[parents[i]].append(i)
        # Calc size of each subtree
        subtrees = dict()
        self.calc_subtrees(adj_list, total, 0, subtrees)
        # Calc score of each node
        max_score, max_count = 0, 0
        for i in range(total):
            score = 1
            remain = total - 1
            for child in adj_list[i]:
                score *= subtrees[child]
                remain -= subtrees[child]
            if remain > 0:
                score *= remain
            if score > max_score:
                max_score = score
                max_count = 1
            elif score == max_score:
                max_count += 1
        return max_count
