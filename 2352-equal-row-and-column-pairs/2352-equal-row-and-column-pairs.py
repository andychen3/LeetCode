from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        row_counts = defaultdict(int)

        for row in grid:
            key = tuple(row)
            row_counts[key] += 1
        
        col_counts = defaultdict(int)
        for col in zip(*grid):
            key = tuple(col)
            col_counts[key] += 1
            
        for key in row_counts:
            ans += row_counts[key] * col_counts[key]
        
        return ans