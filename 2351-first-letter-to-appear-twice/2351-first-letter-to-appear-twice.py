class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash_set = set()
        
        for words in s:
            if words not in hash_set:
                hash_set.add(words)
            else:
                return words