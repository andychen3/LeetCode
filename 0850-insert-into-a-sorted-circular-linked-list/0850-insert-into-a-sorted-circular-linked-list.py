"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = ListNode(insertVal)
            new_node.next = new_node
            return new_node

        curr = head

        while curr.next != head:
            if curr.val <= insertVal <= curr.next.val:
                break
            elif curr.val > curr.next.val and (insertVal > curr.val or insertVal < curr.next.val):
                break

            curr = curr.next


        node = ListNode(insertVal, next=curr.next)
        curr.next = node
        return head