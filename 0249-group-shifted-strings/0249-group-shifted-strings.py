from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        def create_key(word):
            key = []
            for i in range(len(word)-1):
                key.append((ord(word[i+1]) - ord(word[i])) % 26)
            return tuple(key)

        for word in strings:
            key = create_key(word)
            groups[key].append(word)
        
        return list(groups.values())
            