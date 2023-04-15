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
        # use fast and slow pointer and then start reversing mid way
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr = slow
        prev = None
        
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
            
        ptr1 = head
        
        while prev.next:
            ptr1.next, ptr1 = prev, ptr1.next
            prev.next, prev = ptr1, prev.next
        
        
        # start merging the two lists together