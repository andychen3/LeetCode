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
            node = Node(insertVal)
            node.next = node
            return node
        curr = head
        while curr.next != head:
            
            if curr.val <= insertVal <= curr.next.val:
                break
            # curr.val is to find the highest number and where the tail shuld be.
            # curr.val <= insertval is for the condiiton that you are at the tail and you are trying
            # to put a bigger number
            # curr.next.val >= insertVal is for if you reached the tail but the insertval is actually smaller so you have to keep going.
            # We have the while condition to break out if you go back in the cycle so the second condition 
            # curr.next.val >= insertVal solves for the 0 case if the tail element was this [3,5,1] and you are trying to put in a 0 which should go [3,5,0,1]. You need to add the curr.next.val >= insertVal
            if curr.val > curr.next.val and (curr.val <= insertVal or curr.next.val >= insertVal):
                break
            curr = curr.next
        node = Node(insertVal, curr.next)
        curr.next = node
        return head