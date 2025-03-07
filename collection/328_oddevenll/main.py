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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd = head
        even_head, even = head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
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
        ([1,2,3,5],[1,3,2,5]),
        ([1,2],[1,2]),
        ([1,2,3,4,5],[1,3,5,2,4]),
        ([1],[1])
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
        result = solution.oddEvenList(head)
        judge(solution.get_array(result), case[1])
    



    
   
