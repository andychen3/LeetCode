class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = {}
        same_elem = {}
        
        for idx, key in enumerate(list1):
            hash_map[key] = idx
        
        for idx, key in enumerate(list2):
            if key in hash_map:
                same_elem[key] = idx
                same_elem[key] += hash_map[key]
        
        min_val = min(same_elem.values())
        ans = []

        for key, val in same_elem.items():
            if val == min_val:
                ans.append(key)
        return ans
                
        
