# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(next=list1)
        curr = dummy
        
        for _ in range(a):
            curr = curr.next
        
        new_end = curr
        
        for _ in range(b - a + 2):
            curr = curr.next
            
        new_tail = curr
        
        new_end.next = list2
        
        while new_end and new_end.next:
            new_end = new_end.next
        
        new_end.next = new_tail
        return dummy.next