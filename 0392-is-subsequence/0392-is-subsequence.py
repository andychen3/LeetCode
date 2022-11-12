class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = t_ptr = 0
        
        while t_ptr < len(t) and s_ptr < len(s):
            char_s = s[s_ptr]
            char_t = t[t_ptr]
            if char_s == char_t:
                s_ptr += 1
            t_ptr += 1
            
            
        return s_ptr == len(s)