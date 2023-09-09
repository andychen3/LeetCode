from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        arr1 = []
        arr2 = []
        ans = 0
        N = len(img1)

        # get the coordinates for each img
        for r in range(N):
            for c in range(N):
                if img1[r][c]:
                    arr1.append((r,c))
                if img2[r][c]:
                    arr2.append((r,c))
        
        overlaps = defaultdict(int)
        for x1, y1 in arr1:
            for x2, y2 in arr2:
                # Transformation vector
                trans_vector = (x2 - x1, y2-y1)
                # Use the transformation vector as a key and add 1 everytime a pair shares the same vector
                overlaps[trans_vector] += 1
                # Find the max overlap
                ans = max(ans, overlaps[trans_vector])
        return ans