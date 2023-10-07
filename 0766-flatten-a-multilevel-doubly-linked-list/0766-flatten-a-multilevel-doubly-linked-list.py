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
        def merge(curr):
            child = curr.child

            # Iterate through child list
            # We want child.next instead of just child because we only want to iterate through the list
            # if there is an element after child. Because we don't want to set child to null.
            while child.next:
                child = child.next
            
            if curr.next:
                child.next = curr.next
                curr.next.prev = child
            # Go back to the current element before it entered into child list
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None

        while curr:
            if curr.child:
                merge(curr)
            curr = curr.next
        return dummy.next


