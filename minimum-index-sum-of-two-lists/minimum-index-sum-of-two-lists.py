class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_set = collections.Counter(list1)
        list2_set = collections.Counter(list2)
        intersect = list1_set & list2_set

        hash = collections.defaultdict(int)
        res = []
        
        for val in intersect:
            hash[val] += list1.index(val)
            hash[val] += list2.index(val)
        
        min_val = min(hash.values())
        
        for keys, value in hash.items():
            if value == min_val:
                res.append(keys)
                
        return res
        