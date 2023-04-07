from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        arr1 = []
        arr2 = []
        N = len(img1)
        
        for r in range(N):
            for c in range(N):
                if img1[r][c] == 1:
                    arr1.append((r,c))
                if img2[r][c] == 1:
                    arr2.append((r,c))
                    
                    
        ans = 0
        overlaps = defaultdict(int)
        
        for x_a, y_a in arr1:
            for x_b, y_b in arr2:
                vector = (x_b - x_a, y_b - y_a)
                overlaps[vector] += 1
                ans = max(ans, overlaps[vector])
        return ans
                
        