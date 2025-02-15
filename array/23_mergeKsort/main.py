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

def build_linkedlist(array):
    head = None
    prev = None
    for num in array:
        node = ListNode(num)
        if not head: head = node
        if prev: prev.next = node
        prev = node
    return head

def get_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# https://leetcode.com/problems/sort-list/description
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def merge(self, left, right):
        dummy = ListNode()
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right
        return dummy.next

    def merge_divider(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        left = self.merge_divider(lists, start, mid)
        right = self.merge_divider(lists, mid + 1, end)
        return self.merge(left, right)

    @timeit
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        return self.merge_divider(lists, 0, len(lists) - 1)

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
        ([[3,4]], [3,4]),
        ([[]], [])
    ]
    for case in cases:
        lists = []
        for l in case[0]:
            head = build_linkedlist(l)
            lists.append(head)
        result = solution.mergeKLists(lists)
        judge(get_array(result), case[1])
    



    
   