from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = defaultdict(int)

        for idx, word in enumerate(list1):
            for idx2, word2 in enumerate(list2):
                if word == word2:
                    hash_map[word] = idx + idx2
        
        min_val = min(hash_map.values())
        ans = []
        for key, val in hash_map.items():
            if val == min_val:
                ans.append(key)
        return ans