from typing import List

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def swap(first, second, prev):
            if second is None:
                return
            # Swap nodes
            tmp = second.next
            prev.next = second
            second.next = first
            first.next = tmp
            # Can't go futher
            if first.next is None:
                return
            swap(first.next, first.next.next, first)

        dummy = ListNode()
        dummy.next = head
        if dummy.next is not None:
            swap(dummy.next, dummy.next.next, dummy)
        return dummy.next
