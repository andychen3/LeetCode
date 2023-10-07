# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = prev = ListNode(next=head)
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                # We don't do prev = prev.next because to remove vals we always have to be one behind
            else:
                # You only move this when the current element isn't the value
                prev = curr
            curr = curr.next
        return dummy.next 