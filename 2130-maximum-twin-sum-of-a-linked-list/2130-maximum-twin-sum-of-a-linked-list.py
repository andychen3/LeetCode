# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return None
        
        slow = head
        fast = head
        max_sum = 0
        prev = None
        length = 0
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            length += 2
            
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        new_head = head
        
        for i in range(length//2):
            max_sum = max(max_sum, new_head.val + prev.val)
            new_head = new_head.next
            prev = prev.next
        return max_sum