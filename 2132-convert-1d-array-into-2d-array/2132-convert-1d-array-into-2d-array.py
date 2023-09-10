class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if you can even construct the 2d array. The only time it doesnt work
        # is if mxn != length of original array.
        if len(original) != m*n:
            return []

        # Build the 2D array based on given rows and columns
        ans = [[0]*n for _ in range(m)]

        # Iterate through the length of the original array
        for i in range(len(original)):
            # i // n will always give you the correct row from the original array
            # i % n will always give you the correct column.
            ans[i // n][i % n] = original[i]
        return ans