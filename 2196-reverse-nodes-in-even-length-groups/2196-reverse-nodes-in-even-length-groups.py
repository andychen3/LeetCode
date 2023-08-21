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

            # find number of nodes within group
            # It is curr.next because you have to find out if the next element exists
            while curr.next and count < group:
                count += 1
                curr = curr.next

            # Set variables to begin reversal
            prev, curr = tail, tail.next

            if count % 2 == 0:
                # cookie cutter traversal
                while count and curr:
                    next_node = curr.next
                    curr.next = prev

                    prev = curr
                    curr = next_node
                    count -= 1
                # Find start of current group
                first = tail.next
                # Set the current group's first node to connect to next group's first node
                first.next = curr
                # Set last group's end node to the current group's end node
                tail.next = prev
                # Move tail to end node of current group
                tail = first
            else:
                # No reversal
                while count and curr:
                    prev = curr
                    curr = curr.next
                    count -= 1
                tail = prev
            
            group += 1
        return head