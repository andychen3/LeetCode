class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        N = len(image)
        
        # reverse
        for r in range(N):
            image[r].reverse()
            
        # flip 0s and 1s
        
        for r in range(N):
            for c in range(N):
                if image[r][c] == 1:
                    image[r][c] = 0
                else:
                    image[r][c] = 1
        
        return image