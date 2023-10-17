# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        curr.next = head

        k %= length
        new_curr = head

        for _ in range(length - k - 1):
            new_curr = new_curr.next
        new_head = new_curr.next
        new_curr.next = None
        return new_head




