from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        def get_key(word):
            key = []
            for i in range(len(word)-1):
                key.append((ord(word[i+1]) - ord(word[i])) % 26)
            return tuple(key)


        for words in strings:
            key = get_key(words)
            groups[key].append(words)
        return list(groups.values())