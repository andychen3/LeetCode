class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        N = len(image)

        # Flipped the image horizontally
        for rows in image:
            rows.reverse()

        # Invert the image
        for r in range(N):
            for c in range(N):
                # If the image is 1
                if image[r][c]:
                    image[r][c] = 0
                else:
                    image[r][c] = 1
        return image