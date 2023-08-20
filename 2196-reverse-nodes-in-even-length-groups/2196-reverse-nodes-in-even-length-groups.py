# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        group = 2
        tail = head

        while tail and tail.next:
            count = 1
            curr = tail.next

            # Finding the number of nodes in the next group
            while curr.next and count < group:
                curr = curr.next
                count += 1

            prev = tail
            curr = tail.next

            if count % 2 == 0:
                # reverse the nodes in the group
                while count and curr:
                    next_node = curr.next
                    curr.next = prev

                    prev = curr
                    curr = next_node
                    count -= 1
                first = tail.next
                first.next = curr
                tail.next = prev
                tail = first
            else:
                while count and curr:
                    prev = curr
                    curr = curr.next
                    count -= 1
                tail = prev
            
            group += 1
        
        return head
        