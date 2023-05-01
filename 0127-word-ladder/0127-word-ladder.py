from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbors = defaultdict(list)
        # build neighbors list
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)
                
        d = deque([(beginWord, 1)])
        wordList.append(beginWord)
        seen = {beginWord}
                
        while d:
            word, steps = d.popleft()
            if word == endWord:
                return steps
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for chars in neighbors[pattern]:
                    if chars not in seen:
                        seen.add(chars)
                        d.append((chars, steps+1))
        return 0