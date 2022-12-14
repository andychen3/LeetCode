class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        starting_pixel = image[sr][sc]
        
        if image[sr][sc] == color:
            return image
        
        def dfs(x, y):
            if 0 <= x < rows and 0 <= y < cols and image[x][y] == starting_pixel:
                image[x][y] = color
            else:
                return
            
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            
        
        dfs(sr, sc)
        return image
        
        
#         rows = len(image)
#         cols = len(image[0])
        
#         starting_pixel = image[sr][sc]
#         image[sr][sc] = color
#         q = deque([(sr, sc)])
#         seen = set()
        
#         while q:
#             curr_x, curr_y = q.popleft()
        
#             for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
#                 new_x = curr_x+x
#                 new_y = curr_y+y
#                 if 0 <= (new_x) < rows and 0 <= (new_y) < cols and image[new_x][new_y] == starting_pixel:
#                     if (new_x, new_y) not in seen: 
#                         image[new_x][new_y] = color
#                         q.append((new_x, new_y))
#                         seen.add((new_x, new_y))   
#         return image

        
            
        