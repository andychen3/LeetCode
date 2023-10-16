# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        groups = 1
        length = 1
        curr = head
        connect = None

        def reverse(node, n):
            new_curr = node.next
            prev = None
            node_to_start = new_curr

            for _ in range(n):
                temp = new_curr.next
                new_curr.next = prev
                prev = new_curr
                new_curr = temp
            node.next = prev
            node_to_start.next = new_curr
            return node_to_start

        
        while curr:
            # The or not curr.next covers if the last group is odd but there is an even length of nodes
            # And you are at the end of the list. This allows you to go in and reverse the list.
            if groups == length or not curr.next:
                if length % 2 == 0:
                    curr = reverse(connect, length)
                connect = curr
                groups += 1
                length = 0
            length += 1
            curr = curr.next
        return dummy.next