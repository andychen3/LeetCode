class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}
        
        def dfs(node):
            for neighbors in rooms[node]:
                if neighbors not in seen:
                    seen.add(neighbors)
                    dfs(neighbors)
            
        dfs(0)
        print(seen)
        return len(seen) == len(rooms)
        