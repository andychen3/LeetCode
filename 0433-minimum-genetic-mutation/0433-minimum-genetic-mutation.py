from collections import defaultdict, deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        neighbors = defaultdict(list)
        bank.append(startGene)
        
        for words in bank:
            for chars in "ACGT":
                for j in range(len(words)):
                    pattern = words[:j] + chars + words[j+1:]
                    if pattern in bank:
                        neighbors[words].append(pattern)

        
        q = deque([(startGene, 0)])
        seen = {startGene}
        
        while q:
            word, mutations = q.popleft()
            
            for words in neighbors[word]:
                if words == endGene:
                    return mutations+1
                if words not in seen:
                    seen.add(words)
                    q.append((words, mutations+1))
        return -1
            
            