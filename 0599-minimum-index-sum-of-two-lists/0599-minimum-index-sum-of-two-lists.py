from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        intersect = set(list1) & set(list2)
        hash_map = defaultdict(int)

        for idx, word in enumerate(list1):
            if word in intersect:
                hash_map[word] += idx
            
        for idx, word in enumerate(list2):
            if word in intersect:
                hash_map[word] += idx
        
        ans = []
        min_val = min(hash_map.values())

        for key, val in hash_map.items():
            if val == min_val:
                ans.append(key)
        return ans
        
