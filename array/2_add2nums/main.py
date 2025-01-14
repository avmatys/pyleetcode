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

# https://leetcode.com/problems/add-two-numbers/description/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    @timeit
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode(0)
        def sum_nums(l1:Optional[ListNode], l2: Optional[ListNode], res_node: ListNode):
            next_l1 = None
            if l1:
                res_node.val += l1.val
                next_l1 = l1.next
            next_l2 = None
            if l2:
                res_node.val += l2.val
                next_l2 = l2.next
            carry = res_node.val // 10
            res_node.val %= 10
            if carry:   
                res_node.next = ListNode(carry)
            if next_l1 or next_l2:
                if not res_node.next:
                    res_node.next = ListNode(0)
                sum_nums(next_l1, next_l2, res_node.next)
        sum_nums(l1, l2, result_head)
        return result_head
    
    def get_array(self, head: ListNode):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([3,4,5], [1,2,3]), [4,6,8]),
        (([9,4,5], [9,2,3]), [8,7,8]),
        (([9,4,5], [9,2,5]), [8,7,0,1]),
        (([9,9,9,9,9,9,9],[9,9,9,9]), [8,9,9,9,0,0,0,1])
    ]
    for case in cases:
        heads = []
        for arr in case[0]:
            head = None
            prev = None
            for el in arr:
                node = ListNode(el)
                if not head:
                    head = node
                if prev:
                    prev.next = node
                prev = node
            heads.append(head)
        result = solution.addTwoNumbers(*heads)
        judge(solution.get_array(result), case[1])
    



    
   