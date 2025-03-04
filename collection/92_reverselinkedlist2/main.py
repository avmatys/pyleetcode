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

# https://leetcode.com/problems/reverse-linked-list-ii/
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @timeit
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head
        # Create a dummy node to link and link it to the head of the list
        dummy_head = ListNode(0, head) 
        # Find a node, where we should start reversing
        left_prev, curr = dummy_head, head
        for _ in range(left - 1):
            left_prev = curr
            curr = curr.next
        # Reverse part of the list
        prev = None
        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # Update pointers
        left_prev.next.next = curr # Left element should be connected with last elem of the reversed list
        left_prev.next = prev
        return dummy_head.next
        
    def get_array(self, node: ListNode):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,2,3,4,5], 2, 4), [1,4,3,2,5]),
        (([5], 1, 1,), [5])
    ]
    for case in cases:
        head = None
        prev = None
        for val in case[0][0]: 
            node = ListNode(val)
            if not head:
                head = node
            if prev:
                prev.next = node
            prev = node
        result = solution.reverseBetween(head, case[0][1], case[0][2])
        judge(solution.get_array(result), case[1])
    



    
   