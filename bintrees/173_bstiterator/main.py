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


# https://leetcode.com/problems/binary-search-tree-iterator/
class Solution:

    @timeit
    def inorder(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = []
        stack = []
        node = root
        while stack or node is not None:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(str(node.val))
            node = node.right
        return ",".join(result)
    
    @timeit 
    def preorder(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = []
        stack = [root]
        node = root
        while stack:
            node = stack.pop()
            result.append(str(node.val))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ",".join(result)    
    
    @timeit
    def postorder(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "";
        result = []
        stack = []
        node = root
        last_visited = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            peek_node = stack[-1]
            if peek_node.right and peek_node.right != last_visited:
                node = peek_node.right
            else:
                result.append(str(peek_node.val))
                last_visited = stack.pop()
        return ','.join(result)


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.visit = root
        self.stack = []

    def next(self) -> int:
        while self.visit:
            self.stack.append(self.visit)
            self.visit = self.visit.left
        next_node = self.stack.pop()
        self.visit = next_node.right
        return next_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.visit is not None

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3,4,5,6], ['4,2,5,1,6,3', '1,2,4,5,3,6', '4,5,2,6,3,1'])
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.inorder(input)
        judge(result, expected[0])
        result = solution.preorder(input)
        judge(result, expected[1])
        result = solution.postorder(input)
        judge(result, expected[2])

    
   