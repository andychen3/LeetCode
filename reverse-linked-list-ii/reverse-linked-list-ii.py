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
        
        for i in range(1, left):
            prev = curr
            curr = curr.next
            
        second_prev = prev
        
        for i in range(right - left + 1):
            curr.next, curr, second_prev = second_prev, curr.next, curr
        
        prev.next.next = curr
        prev.next = second_prev
        
        return dummy.next