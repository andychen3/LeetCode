from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        
        for index, s_char in enumerate(s):
            t_char = t[index]
            if s_char in s_map and s_map[s_char] != t_char:
                return False
            if t_char in t_map and t_map[t_char] != s_char:
                return False
            s_map[s_char] = t_char
            t_map[t_char] = s_char
                
        return True