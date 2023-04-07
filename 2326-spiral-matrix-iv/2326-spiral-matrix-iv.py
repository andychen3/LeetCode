# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        
        def valid(r, c):
            return r < 0 or r >= m or c < 0 or c >= n or matrix[r][c] != -1
        
        x, y = 0, 0
        dx, dy = 0, 1
        
        while head:
            matrix[x][y] = head.val
            
            if valid(x+dx, y+dy):
                dx, dy = dy, -dx
            
            x += dx
            y += dy
            head = head.next
        return matrix