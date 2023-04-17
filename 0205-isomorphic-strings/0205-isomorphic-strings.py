from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        
        for index, char in enumerate(s):
            left_char = t[index]
            if char in s_map and t_map[left_char] != char:
                return False
            if left_char in t_map and s_map[char] != left_char:
                return False
            s_map[char] = left_char
            t_map[left_char] = char
        return True