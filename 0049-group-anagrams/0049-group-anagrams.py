class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        
        for word in strs:
            counts[tuple(sorted(word))].append(word)
        return list(counts.values())