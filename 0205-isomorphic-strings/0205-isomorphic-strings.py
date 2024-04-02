from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = defaultdict(str)
        t_map = defaultdict(str)
        
        for i, char in enumerate(s):
            if char not in s_map and t[i] not in t_map:
                s_map[char] = t[i]
                t_map[t[i]] = char
            
            if s_map[char] != t[i] or t_map[t[i]] != char:
                return False
        return True
            
            