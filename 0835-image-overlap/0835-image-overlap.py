from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        transform = defaultdict(int)
        
        arr1 = []
        arr2 = []
        N = len(img1)
        
        for rows in range(N):
            for col in range(N):
                if img1[rows][col] == 1:
                    arr1.append((rows,col))
                if img2[rows][col] == 1:
                    arr2.append((rows,col))

        ans = 0                    
        for ax, ay in arr1:
            for bx, by in arr2:
                vector = (bx - ax, by - ay)
                transform[vector] += 1
                ans = max(ans, transform[vector])
        return ans