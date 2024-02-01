from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for words in strs:
            key = tuple(sorted(words))
            anagrams[key].append(words)
        return list(anagrams.values())