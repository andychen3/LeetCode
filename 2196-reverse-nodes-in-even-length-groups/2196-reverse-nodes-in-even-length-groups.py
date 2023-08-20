# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        group = 2
        tail = head  # The tail of the previous group
        
        while tail and tail.next:
            cnt = 1  # Actual size of the current group
            cur = tail.next  # First node of the current group
            
            # Calculate the size of the current group
            while cur.next and cnt < group:
                cur = cur.next
                cnt += 1
            
            pre, cur = tail, tail.next
            
            if cnt % 2 == 0:  # If group size is even
                while cnt and cur:
                    nxt = cur.next
                    cur.next = pre
                    pre = cur
                    cur = nxt
                    cnt -= 1
                first = tail.next  # First node of the original group
                first.next = cur
                tail.next = pre
                tail = first
            else:
                while cnt and cur:
                    pre, cur = cur, cur.next
                    cnt -= 1
                tail = pre
            
            group += 1
        
        return head
