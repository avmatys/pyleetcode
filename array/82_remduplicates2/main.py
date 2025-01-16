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

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @timeit
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                if prev:
                    prev.next = curr.next
                else: 
                    head = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
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
        ([1,2,3,3,3,4,4,4,5], [1,2,5]),
        ([0,0,0], []),
        ([], []),
        ([1,2,3], [1,2,3]),
        ([1,1,1,3], [3])
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
        result = solution.deleteDuplicates(head)
        judge(solution.get_array(result), case[1])
    



    
   