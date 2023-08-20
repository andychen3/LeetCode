# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head

        # find the middle
        while fast:
            slow = slow.next
            fast = fast.next.next
        
        # slow should be at the middle.
        # reverse the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev

            prev = slow
            slow = next_node
        
        # find sum
        max_sum = 0

        while head.next:
            max_sum = max(prev.val + head.val, max_sum)
            head = head.next
            prev = prev.next
        
        return max_sum
        