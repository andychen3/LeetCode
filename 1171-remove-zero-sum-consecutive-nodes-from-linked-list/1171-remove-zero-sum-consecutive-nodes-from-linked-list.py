# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefix = 0
        prefix_map = {}
        curr = dummy
        while curr:
            prefix += curr.val
            prefix_map[prefix] = curr
            curr = curr.next
            
        prefix = 0
        curr = dummy
        while curr:
            prefix += curr.val
            if prefix in prefix_map:
                curr.next = prefix_map[prefix].next
            curr = curr.next
        return dummy.next