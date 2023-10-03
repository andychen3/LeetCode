from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = defaultdict(str)
        t_map = defaultdict(str)

        for c1, c2 in zip(s, t):
            if (c1 not in s_map) and (c2 not in t_map):
                s_map[c1] = c2
                t_map[c2] = c1
            elif s_map[c1] != c2 or t_map[c2] != c1:
                return False
        return True