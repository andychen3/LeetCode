# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(next=head)
        prev = dummy
        curr = head
        
        while curr and curr.next:
            first = curr
            second = curr.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            curr = curr.next
        return dummy.next
        