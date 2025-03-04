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

# https://leetcode.com/problems/partition-list/
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @timeit
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        bhead = ListNode()
        shead = ListNode()
        bcurr = bhead
        scurr = shead
        curr = head
        while curr:
            if curr.val < x:
                scurr.next = curr
                scurr = scurr.next
            else:
                bcurr.next = curr
                bcurr = bcurr.next
            curr = curr.next
        scurr.next = bhead.next # bhead.next because bhead is dummy node
        bcurr.next = None
        return shead.next # shead is a dummy one, next is correct
        
    def get_array(self, node: ListNode):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,4,3,2,5,2], 3), [1,2,2,4,3,5]),
        (([2,1], 2), [1,2])
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
        result = solution.partition(head, case[0][1])
        judge(solution.get_array(result), case[1])
    



    
   