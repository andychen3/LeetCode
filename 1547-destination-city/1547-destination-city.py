class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = {}

        for x, y in paths:
            start[x] = y
        
        for destination in start.values():
            if destination not in start:
                return destination
        return -1
            
        