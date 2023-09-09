from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # You can see that the problem wants you to flatten a 2d matrix
        # based on their diagonals. Since the diagonal direction is moving from
        # top-left to bottom right. We should use the anti_diagonals. All numbers in a matrix
        # share a unique sum value based on their diagonals or anti-diagonals when you do r-c or r+c 
        # respectively.

        # So we can group all the numbers based on their anti-diagonals. A great data structure that allows
        # you to access it easily would be to use a hash map to build the sums as keys to the hash

        # Another thing is that you can notice that when you build the ans array every even diagonal are 
        # reversed. So when we iterate through the hashmap we can remember that when the anti-diagonal is
        # even we reverse the array. Because when we build the hash map the array of values are built in
        # sorted order

        anti_diagonals = defaultdict(list)
        rows, cols = len(mat), len(mat[0])
        ans = []

        # traverse the matrix
        for r in range(rows):
            for c in range(cols):
                anti_diagonals[r + c].append(mat[r][c])
        
        # Iterate through hash map to build answer
        for key, values in anti_diagonals.items():
            if key % 2 == 0: # if even diagonal
                # The reason why we don't append is ebcause we are flatten the 2d matrix
                # if we append it would be a list of the values
                ans += values[::-1] # Reverse the list
            else:
                ans += values # We add to the array because in python += is extending the array
        return ans
