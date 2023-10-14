# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        curr = head
        max_sum = 0
        while prev:
            max_sum = max(max_sum, curr.val + prev.val)
            prev = prev.next
            curr = curr.next
        return max_sum