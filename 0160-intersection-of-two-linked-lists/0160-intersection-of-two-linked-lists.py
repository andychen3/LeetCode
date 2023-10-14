# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hA = headA
        hB = headB

        while hA != hB:
            hA = hA.next if hA else headB
            hB = hB.next if hB else headA
        return hA
