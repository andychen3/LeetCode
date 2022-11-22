# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        prev = None
        
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev
        
#         def reverse(node, prev):
#             if not node:
#                 return
            
#             temp, node.next, prev = node.next, prev, node
            
#             return head
            
            
        
#         prev = None
#         return reverse(head, prev)
        
        


        
        

        
        
        