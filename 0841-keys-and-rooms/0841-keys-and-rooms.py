class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            for neighbors in rooms[node]:
                if neighbors not in seen:
                    seen.add(neighbors)
                    dfs(neighbors)
        
        seen = {0}
        dfs(0)
        return len(seen) == len(rooms) 
        
        