# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None
        
        slow, fast = head, head
        dummy = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reversing
        curr = slow
        next_prev = None
        
        while curr:
            curr.next, curr, next_prev = next_prev, curr.next, curr
        
        while next_prev:
            if next_prev.val != dummy.val:
                return False
            next_prev = next_prev.next
            dummy = dummy.next
        
        return True
            