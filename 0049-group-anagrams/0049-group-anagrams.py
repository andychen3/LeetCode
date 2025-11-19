from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)

        for word in strs:
            word_dict[tuple(sorted(word))].append(word)
        
        return list(word_dict.values())