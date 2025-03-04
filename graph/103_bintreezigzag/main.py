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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr, i = 0):
    root = None
    n = len(arr)
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = build_tree(arr, 2 * i + 1)
        root.right = build_tree(arr, 2 * i + 2)
    return root


# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
class Solution:

    @timeit
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root]) 
        result = []
        level = 0
        reverse = False
        while queue:
            if len(result) <= level:
                result.append([])
            size = len(queue)
            buffer = []
            for _ in range(size):
                node = queue.popleft()
                if reverse:
                    buffer.append(node.val)
                else:
                    result[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverse:
                while buffer:
                    result[level].append(buffer.pop())
            reverse = not reverse
            level += 1
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    for i in range(len(result)):       
        assert result[i] == expected[i]


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3,9,20,None,None,15,7], [[3],[20,9],[15,7]]),
        ([1,2,3,4,None,None,5], [[1],[3,2],[4,5]]),
        ([1], [[1]]),
        ([], [])
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.zigzagLevelOrder(input)
        judge(result, expected)
    
   