from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = defaultdict(int)
        same_word = defaultdict(int)

        for idx, word in enumerate(list1):
            hash_map[word] = idx
        
        for idx1, word in enumerate(list2):
            if word in hash_map:
                same_word[word] = idx1 + hash_map[word]
        
        min_val = min(same_word.values())
        ans = []

        for key, val in same_word.items():
            if val == min_val:
                ans.append(key)
        return ans
