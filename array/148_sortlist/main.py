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

    def mergeSort(self, head, n):
        if n < 2:
            return head
        if n == 2:
            if head.val > head.next.val:
                tmp = head.next
                head.next.next = head
                head.next = None
                return tmp
            return head
        # Split into 2 subarrays
        offset = n // 2
        left, right, prev_right = head, head, head
        for i in range(offset):
            prev_right = right
            right = right.next
        prev_right.next = None
        # Solve subproblem
        left = self.mergeSort(left, offset)
        right = self.mergeSort(right, n-offset)
        # Merge back
        return self.merge(left, right)
        

    @timeit
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node, n = head, 0
        while node:
            node = node.next
            n += 1
        head = self.mergeSort(head, n)
        return head

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3,2], [2,3]),
        ([3,4,2], [2,3,4]),
        ([-10,-9,0,1,2], [-10,-9,0,1,2]),
        ([-1,5,3,4,0], [-1,0,3,4,5]),
        ([], [])
    ]
    for case in cases:
        head = build_linkedlist(case[0])
        result = solution.sortList(head)
        judge(get_array(result), case[1])
    



    
   