# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head)

        prev = dummy
        curr = head

        for _ in range(left - 1):
            prev = curr
            curr = curr.next
        
        # Reverse list
        second_prev = prev
        reversed_tail = curr

        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = second_prev

            second_prev = curr
            curr = next_node

        prev.next = second_prev
        reversed_tail.next = curr

        return dummy.next