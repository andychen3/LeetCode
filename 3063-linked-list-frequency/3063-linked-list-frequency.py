# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counts = Counter()
        dummy = ListNode()
        new_head = dummy
        
        curr = head
        
        while curr:
            counts[curr.val] += 1
            curr = curr.next
        
        for val in counts.values():
            new_head.next = ListNode(val)
            new_head = new_head.next
        
        return dummy.next
        
        