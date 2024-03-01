from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)
                
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        
        while queue:
            word, steps = queue.popleft()
            
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for match in graph[pattern]:
                    if match not in seen:
                        seen.add(match)
                        queue.append((match, steps+1))
        return 0