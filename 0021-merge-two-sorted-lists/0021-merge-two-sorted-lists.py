# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode(0)
        dummy = new_list
        
        
        l1 = list1
        l2 = list2
        
        while l1 and l2:
            if l1.val <= l2.val:
                new_list.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                new_list.next = l2
                l2 = l2.next
            new_list = new_list.next
            
        if l1:
            new_list.next = l1
            
        if l2:
            new_list.next = l2
        
        return dummy.next
                