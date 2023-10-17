"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = ListNode(next=head)
        curr = head

        def expand(node):
            child = node.child

            while child.next:
                child = child.next

            if node.next:
                child.next = node.next
                node.next.prev = child
            node.next = node.child
            node.child.prev = node
            node.child = None

        while curr:
            if curr.child:
                expand(curr)
            curr = curr.next
        return dummy.next