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
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def build_tree(arr, i = 0):
    root = None
    n = len(arr)
    if i < n and arr[i] is not None:
        root = Node(arr[i])
        root.left = build_tree(arr, 2 * i + 1)
        root.right = build_tree(arr, 2 * i + 2)
    return root

def next_ptr_to_arr(node: Node):
    result = []
    while node:
        temp = node
        while temp:
            result.append(temp.val)
            temp = temp.next
            if not temp:
                result.append(None)
        node = node.left
    return result


# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
class Solution:

    def connect(self, root: 'Node') -> 'Node':
        prev = root # Start at a root level
        while prev: # We will iterate through the one level nodes, to the right side
            dummy = Node(0) # Create a new node which will be like before real node, to the left side
            curr = dummy # Start iteration like before the real node
            while prev: # Iterate through all items in the one layer from the left to the rigth
                if prev.left:
                    curr.next = prev.left
                    curr = curr.next
                if prev.right:
                    curr.next = prev.right
                    curr = curr.next
                prev = prev.next 
            prev = dummy.next # This will look to the most level node in the next level
        return root
            
    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3,4,5,None,7], [1,None,2,3,None,4,5,7,None]),
        ([], [])
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.connect(input)
        judge(next_ptr_to_arr(input), expected)

    
   