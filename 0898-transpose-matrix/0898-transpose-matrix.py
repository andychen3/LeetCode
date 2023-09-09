class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [ans for ans in list(zip(*matrix))]