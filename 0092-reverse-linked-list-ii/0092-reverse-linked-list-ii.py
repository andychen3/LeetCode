# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        curr = head

        for _ in range(left - 1):
            prev = curr
            curr = curr.next

        reversing_prev = prev
        reversed_tail = curr

        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = reversing_prev

            reversing_prev = curr
            curr = temp
        
        prev.next = reversing_prev
        reversed_tail.next = curr
        return dummy.next