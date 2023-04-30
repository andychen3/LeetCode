from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        visit = {beginWord}
        q = deque([(beginWord, 1)])
        
        while q:
            word, steps = q.popleft()

            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for words in nei[pattern]:
                    if word == endWord:
                        return steps
                    if words not in visit:
                        visit.add(words)
                        q.append((words, steps+1))
        return 0
        