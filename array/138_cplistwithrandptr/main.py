from typing import List, Optional
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

# https://leetcode.com/problems/copy-list-with-random-pointer/
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:

    @timeit
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        print(self.get_array(head))
        if not head:
            return head
        # Add copy after current node: X -> CP_X -> Y -> CP_Y
        node = head
        while node:
            copy_node = Node(node.val)
            tmp = node.next
            node.next = copy_node
            copy_node.next = tmp
            node = tmp
        # We can set random links: CP_X.random = X.random.next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        # Create 2 separate lists
        node = head
        cp_head = node.next
        cp_node = cp_head
        while node:
            node.next = node.next.next
            node = node.next
            if cp_node.next:
                cp_node.next = cp_node.next.next
                cp_node = cp_node.next
        return cp_head
    
    def get_array(self, node: Node):
        result = []
        while node:
            result.append([node.val, node.random.val if node.random else None])
            node = node.next
        return result

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[7,None],[13,0],[11,4],[10,2],[1,0]], [[7,None],[13,7],[11,1],[10,11],[1,7]]),
        ([[1,1],[2,1]], [[1,2],[2,2]]),
        ([[3,None],[3,0],[3,None]], [[3,None],[3,3],[3,None]])
    ]
    for case in cases:
        head = None
        prev = None
        nodes = []
        for pair in case[0]:  
            node = Node(pair[0])
            if not head:
                head = node
            if prev:
                prev.next = node
            prev = node
            nodes.append(node)
        for idx, pair in enumerate(case[0]):
            if pair[1] is not None:
                nodes[idx].random = nodes[pair[1]]
        result = solution.copyRandomList(head)
        judge(solution.get_array(result), case[1])
    



    
   