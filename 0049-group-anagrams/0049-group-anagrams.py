from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            hash_map[key].append(word)
        
        return list(hash_map.values())