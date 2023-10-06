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
            curr = Node(insertVal)
            curr.next = curr
            return curr

        

        curr = head
        while curr.next != head:
            if curr.val <= insertVal <= curr.next.val:
                break
            if curr.val > curr.next.val and (curr.val <= insertVal or insertVal <= curr.next.val):
                break
            curr = curr.next
        
        node = Node(insertVal, next=curr.next)
        curr.next = node
        
        return head
