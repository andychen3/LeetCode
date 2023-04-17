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
        if not head:
            return
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow
        prev = None
        
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        
        # merge the list
          
        first_ptr = head
        second_ptr = prev
        
        while second_ptr.next:
            first_ptr.next, first_ptr = second_ptr, first_ptr.next
            second_ptr.next, second_ptr = first_ptr, second_ptr.next
        
        return head
        
            