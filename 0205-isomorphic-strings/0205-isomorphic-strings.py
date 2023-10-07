from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = defaultdict(str)
        t_map = defaultdict(str)

        for s_char, t_char in zip(s, t):
            if s_char not in s_map and t_char not in t_map:
                s_map[s_char] = t_char
                t_map[t_char] = s_char
            if s_map[s_char] != t_char or t_map[t_char] != s_char:
                return False
        return True