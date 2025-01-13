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

# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    @timeit
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    
    def get_array(self, head: ListNode):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(3)
    e1 = ListNode(4)
    head.next = e1
    e2 = ListNode(5)
    e1.next = e2
    head2 = ListNode(0)
    e12 = ListNode(1)
    head2.next = e12
    e22 = ListNode(2)
    e12.next = e22
    judge(solution.get_array(solution.mergeTwoLists(head, head2)), [0,1,2,3,4,5])
    



    
   