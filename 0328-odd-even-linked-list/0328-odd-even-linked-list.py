# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd, even = head, head.next
        even_head = even
        dummy = ListNode(next=head)
        curr = head.next.next
        count = 3

        while curr:
            if count % 2:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            curr = curr.next
            count += 1
        even.next = None
        odd.next = even_head
        return dummy.next
