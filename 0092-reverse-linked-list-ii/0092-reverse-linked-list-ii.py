# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = prev = ListNode(next=head)
        curr = head


        for _ in range(left-1):
            prev = curr
            curr = curr.next
        
        reversed_prev = prev
        reversed_tail = curr

        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = reversed_prev
            reversed_prev = curr
            curr = temp
        
        prev.next = reversed_prev
        reversed_tail.next = curr
        return dummy.next