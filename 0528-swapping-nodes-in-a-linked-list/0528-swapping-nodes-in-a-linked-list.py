# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = fast = head
        node_to_switch = None

        for _ in range(k-1):
            fast = fast.next
        node_to_switch = fast

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        node_to_switch.val, slow.val = slow.val, node_to_switch.val

        return dummy.next

