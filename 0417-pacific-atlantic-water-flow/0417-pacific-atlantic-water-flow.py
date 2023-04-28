class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        
        p_visited = set()
        a_visited = set()
        rows, cols = len(heights), len(heights[0])
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        
        def traverse(x, y, visited):
            if (x, y) in visited:
                return
            visited.add((x, y))
            for dx, dy in directions:
                new_x, new_y = dx + x, dy + y
                if valid(new_x, new_y):
                    if heights[new_x][new_y] >= heights[x][y]:
                        traverse(new_x, new_y, visited)
        
        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols-1, a_visited)
        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows-1, col, a_visited)
        
        return list(p_visited & a_visited)