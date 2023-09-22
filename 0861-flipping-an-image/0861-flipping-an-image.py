class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        # Flip image
        for row in image:
            row.reverse()

        n = len(image)

        for r in range(n):
            for c in range(n):
                if image[r][c]:
                    image[r][c] = 0
                else:
                    image[r][c] = 1
        return image


        