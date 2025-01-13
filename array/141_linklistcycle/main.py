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

# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(3)
    e1 = ListNode(4)
    head.next = e1
    e2 = ListNode(5)
    e1.next = e2
    e2.next = head
    assert solution.hasCycle(head) == True
    head = ListNode(3)
    e1 = ListNode(4)
    head.next = e1
    e2 = ListNode(5)
    e1.next = e2
    assert solution.hasCycle(head) == False
    



    
   