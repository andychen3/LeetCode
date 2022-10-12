class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = collections.defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            hash[sorted_word].append(word)

        return list(hash.values())
        