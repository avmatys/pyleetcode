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

# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @timeit
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Split into 2 linked lists
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right_head = slow.next
        slow.next = None
        # Reverse right linked list
        prev, curr = None, right_head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        right_head = prev
        # Calc max sums
        max_sum = float('-inf')
        left, right = head, right_head
        while left and right:
            max_sum = max(left.val + right.val, max_sum)
            left = left.next
            right = right.next
        return max_sum


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3,5], 6),
        ([1,2],3),
        ([1,2,3,4,100,0], 102),
        ([1,2,1000,2000,0,0], 3000)
    ]
    for case in cases:
        head = None
        prev = None
        for val in case[0]: 
            node = ListNode(val)
            if not head:
                head = node
            if prev:
                prev.next = node
            prev = node
        result = solution.pairSum(head)
        judge(result, case[1])
    



    
   
