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
        beginning = odd
        
        while odd and odd.next:
            temp = odd.next.next
            odd.next = odd.next.next
            if odd.next == None:
                break
            odd = temp
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        return beginning
            
            

        
        