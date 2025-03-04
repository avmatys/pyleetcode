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

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @timeit
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        node = head
        while node:
            size += 1
            node = node.next
        if size == 0 or n > size:
            return head
        if size == n:
            return head.next
        k = size - n - 1
        node = head
        while k > 0:
            node = node.next
            k -= 1
        node.next = node.next.next
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
        (([1,2,3,4,5], 2), [1,2,3,5]),
        (([0,1,2], 1), [0,1]),
        (([1,2], 2), [2]),
        (([1], 2), [1])
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
        result = solution.removeNthFromEnd(head, case[0][1])
        judge(solution.get_array(result), case[1])
    



    
   