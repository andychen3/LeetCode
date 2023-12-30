from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_counts = Counter(word1)
        word2_counts = Counter(word2)
        print(word1_counts.values())
        print(word2_counts.values())        
        return word1_counts.keys() == word2_counts.keys() and sorted(word1_counts.values()) == sorted(word2_counts.values())