# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0, head)
        curr = head

        while curr:
            if curr.val == val:
                dummy.next = curr.next
                curr = curr.next
            elif curr.next and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next