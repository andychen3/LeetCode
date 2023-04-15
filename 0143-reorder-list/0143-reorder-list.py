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
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        ptr1 = head
        
        while prev.next:
            temp = ptr1.next
            ptr1.next = prev
            temp2 = prev.next
            prev.next = temp
            ptr1 = temp
            prev = temp2
        
        
        # start merging the two lists together