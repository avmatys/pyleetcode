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

# https://leetcode.com/problems/reverse-linked-list/description/
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @timeit
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = None # this is a head, but initially this is an end of the list
        current = head
        while current:
            tmp = current.next # store next element as we will crash link to the next
            current.next = reversed_head # 1 element will be the last one
            reversed_head = current # Store current enty as an element of the reversed list
            current = tmp # go to the next one, as we crashed link
        return reversed_head
        
    def get_array(self, node: ListNode):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,4,3,2,5,2], [2,5,2,3,4,1]),
        ([2,1], [1,2])
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
        result = solution.reverseList(head)
        judge(solution.get_array(result), case[1])
    



    
   