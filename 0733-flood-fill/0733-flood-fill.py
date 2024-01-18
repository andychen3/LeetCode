class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        original_color = image[sr][sc]
        rows, col = len(image), len(image[0])
        
        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= col or image[x][y] != original_color:
                return
            
            image[x][y] = color
            
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        dfs(sr, sc)
        return image
            
            