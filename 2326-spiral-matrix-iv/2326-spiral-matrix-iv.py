# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:        
        res = [[-1]*n for _ in range(m)]
        
        # if the next point is out of bounds or is on a previous number we have to change directions
        def valid(r, c):
            return 0 > r or r >= m or 0 > c or c >= n or res[r][c] != -1
        
        x, y = 0, 0
        dx, dy = 0, 1
        
        while head:
            res[x][y] = head.val
            
            if valid(x+dx, y+dy):
                dx, dy = dy, -dx
            
            x += dx
            y += dy
            head = head.next
        
        return res