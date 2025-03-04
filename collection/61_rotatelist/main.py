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

# https://leetcode.com/problems/rotate-list/description/
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @timeit
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Get number of elements in linked list
        def ll_len(node: ListNode):
            len = 0
            while node:
                len += 1
                node = node.next
            return len
         # Basic check
        length = ll_len(head)
        if k == 0 or length == 0 or k % length == 0:
            return head
         # Calc nums of rotation
        rotation = k % length
        rotated_head = head
        tail = head # tail of the current list -> should be connected with head
        node = head
        i = 0
        while node:
            i += 1
            tail = node
            if i == length - rotation:
                tmp = node.next # Rotated elem. This should be a new head
                node.next = None # Make 2 lists around rotated element
                rotated_head = tmp
                node = tmp
            else:
                node = node.next
        # Reconnect list
        tail.next = head
        return rotated_head
        

    def get_array(self, node: ListNode):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,2,3,4,5], 2), [4,5,1,2,3]),
        (([0,1,2], 4), [2,0,1]),
        (([0,1,2], 0), [0,1,2]),
        (([], 0), [])
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
        result = solution.rotateRight(head, case[0][1])
        judge(solution.get_array(result), case[1])
    



    
   