class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(curr, index):
            
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.end
        
        
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)