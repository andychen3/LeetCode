class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_hash = {}
        s_hash = {}
        new_s = s.split(" ")
        
        if len(pattern) != len(new_s):
            return False
        
        for val1, val2 in zip(pattern, new_s):
            if val1 not in pattern_hash and val2 not in s_hash:
                pattern_hash[val1] = val2
                s_hash[val2] = val1
            elif pattern_hash.get(val1) != val2 or s_hash.get(val2) != val1:
                
                return False
        return True
        
