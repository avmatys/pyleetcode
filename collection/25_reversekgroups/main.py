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

# https://leetcode.com/problems/reverse-nodes-in-k-group/
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @timeit
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(head: ListNode, prev: ListNode, k):
            for _ in range(k):
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            return head

        if k <= 1:
            return head   
        dummy = ListNode(0, head)
        prev_head_group = dummy # Pointer, which shows an element before current group
        count = 1
        curr_node = head
        head_group = None
        while curr_node:
            # Start of a new group
            if count % k == 1:
                head_group = curr_node
            # End of the the group - reverse it and attach to the full list
            elif count % k == 0:
                prev = curr_node.next # Element, which goes after current node should be before first element in the reversed group
                reverse(head_group, prev, k) # Simply reverse a group from the beginning
                prev_head_group.next = curr_node # curr node before reverse was last element in the group, but not this is a first one
                prev_head_group = head_group # and start will be we end of a current group and next before group
                curr_node = head_group # update current node - start will be the end as it's reversed
            count += 1
            curr_node = curr_node.next
        return dummy.next
        
    def get_array(self, node: ListNode):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,2,3,4,5], 2), [2,1,4,3,5]),
        (([1,2,3,4,5], 3), [3,2,1,4,5]),
        (([5,4,1],1), [5,4,1])
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
        result = solution.reverseKGroup(head, case[0][1])
        judge(solution.get_array(result), case[1])
    



    
   