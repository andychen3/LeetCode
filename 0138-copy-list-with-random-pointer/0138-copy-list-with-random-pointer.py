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
        hash_map = {None: None}

        curr = head

        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        
        while curr:
            new_list = hash_map[curr]
            if curr.random:
                new_list.random = hash_map[curr.random]
            if curr.next:
                new_list.next = hash_map[curr.next]
            curr = curr.next
        return hash_map[head]