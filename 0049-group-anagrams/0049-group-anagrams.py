from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_hash = defaultdict(list)
        
        for vals in strs:
            group_hash[tuple(sorted(vals))].append(vals)
            
        return list(group_hash.values())