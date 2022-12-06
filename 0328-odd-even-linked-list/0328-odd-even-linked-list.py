# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        even = head.next
        evenHead = even
        odd = head
        
        while even and even.next:
            temp = odd.next.next
            odd.next = odd.next.next
            odd = temp
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        return head
            
            

        
        