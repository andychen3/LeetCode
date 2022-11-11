class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        count = collections.defaultdict(int)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                count[mat[i][j]] += 1
        
        for key, value in count.items():
            if value == len(mat):
                return key
        
        return -1
        