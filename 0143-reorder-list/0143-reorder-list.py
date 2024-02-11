# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        curr = head
        
        while prev.next:
            temp1 = curr.next
            temp2 = prev.next
            curr.next = prev
            prev.next = temp1
            curr = temp1
            prev = temp2
        
        return head
            