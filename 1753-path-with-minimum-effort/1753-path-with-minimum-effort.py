class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # First impression is that I will have to use some of graph traversal
        # Second is that since it's asking for min effort across this could be greedy.
        # I am looking for min effort so i'm looking for a threshold. This means
        # it is binary search while using a graph traversal to move through the matrix

        def valid(r, c):
            return 0 <= r < row and 0 <= c < col

        def check(effort):
            stack = [(0, 0)]
            seen = {(0,0)}
            directions = ((0,1), (1,0), (-1,0), (0,-1))

            while stack:
                x, y = stack.pop()

                if (x, y) == (row - 1, col - 1):
                    return True

                for dx, dy in directions:
                    next_row, next_col = dx + x, dy + y
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        # If the absolute different between the next cell with current cell
                        # is within the range of effort you can move to it
                        if abs(heights[next_row][next_col] - heights[x][y]) <= effort:
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
            return False

        row = len(heights)
        col = len(heights[0])
        left = 0
        right = max(max(row) for row in heights)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

        
            