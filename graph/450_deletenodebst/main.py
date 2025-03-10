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

# https://leetcode.com/problems/search-in-a-binary-search-tree/
class Solution:

    def delete_root_node(self, root):
        if root is None:
            return None
        # Return another subtree
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # Have both subtrees
        next = root.right
        prev = None
        while next.left:
            prev = next
            next = next.left
        # Attach left part of the original tree to the smallest part of the right side
        next.left = root.left
        # Balance a tree
        if next != root.right:
            prev.left = next.right
            next.right = root.right
        # Return new
        return next

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        del_node = root
        prev_del_node = None
        # Find node to delete
        while del_node and del_node.val != key:
            prev_del_node = del_node
            if del_node.val < key:
                del_node = del_node.right
            else:
                del_node = del_node.left
        # Node to delete is a root
        if prev_del_node == None:
            return self.delete_root_node(root)
        # Node to delete is in the left subtree
        if prev_del_node.left == del_node:
            prev_del_node.left = self.delete_root_node(del_node)
        else:
            prev_del_node.right = self.delete_root_node(del_node)
        return root

    
   
