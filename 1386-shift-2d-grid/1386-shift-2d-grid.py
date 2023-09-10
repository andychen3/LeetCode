class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        
        rows = len(grid)
        cols = len(grid[0])

        ans = [[0 for _ in range(cols)]for _ in range(rows)]
        
        for i in range((rows*cols)):
            # We need to mod i+k by the total row*cols before indexing into the new array because
            # We want to make sure that when you add k to i it is still within bounds of the original array
            # For example if we didnt have this line. When we try to index in at the end of the array.
            # The row will go out of bounds.
            # While if we have this line when we reach the last element when modded with the end of the list
            # we get the wraparound.
            index = (i + k) % (rows*cols)
            ans[index  // cols][index % cols] = grid[i //cols][i % cols]
        return ans