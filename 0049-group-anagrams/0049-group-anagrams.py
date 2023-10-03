from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for words in strs:
            groups[tuple(sorted(words))].append(words)
        
        return [vals for vals in groups.values()]