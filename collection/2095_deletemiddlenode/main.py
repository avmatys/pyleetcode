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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head 
    
    def get_array(self, node: ListNode):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3,5],[1,2,5]),
        ([1,2],[1]),
        ([1,2,3,4,5],[1,2,4,5]),
        ([1],[])
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
        result = solution.deleteMiddle(head)
        judge(solution.get_array(result), case[1])
    



    
   
