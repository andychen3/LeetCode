# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = new_list = ListNode()
        heap = []
        
        for index, ll in enumerate(lists):
            if ll:
                heappush(heap, (ll.val, index))
                
        while heap:
            val, idx = heappop(heap)
            new_list.next = ListNode(val)
            new_list = new_list.next
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heappush(heap, (lists[idx].val, idx))
        
        return head.next