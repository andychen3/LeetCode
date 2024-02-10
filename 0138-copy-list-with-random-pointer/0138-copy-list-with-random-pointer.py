"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {None:None}
        curr = head
        
        while curr:
            new_node = Node(curr.val)
            copy[curr] = new_node
            curr = curr.next
            
        curr = head
        
        while curr:
            new_node = copy[curr]
            new_node.next = copy[curr.next]
            new_node.random = copy[curr.random]
            curr = curr.next
        
        return copy[head]