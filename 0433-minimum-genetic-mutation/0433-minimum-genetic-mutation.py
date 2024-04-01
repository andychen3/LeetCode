from collections import defaultdict, deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        seen = {(startGene)}
        moves = set(bank)
        
        def bfs(node):
            ans = []
            for i in range(8):
                for char in "ACGT":
                    ans.append(node[:i] + char + node[i+1:])
            return ans
        
        while queue:
            node, steps = queue.popleft()
            
            if node == endGene:
                return steps
            
            for neighbor in bfs(node):
                if neighbor in bank and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))
        return -1