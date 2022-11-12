class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hash = collections.defaultdict(int)
        t_hash = collections.defaultdict(int)
        
        for index, s_char in enumerate(s):
            t_char = t[index]
            if s_char not in s_hash and t_char not in t_hash:
                s_hash[s_char] = t_char
                t_hash[t_char] = s_char
            else:
                if s_char in s_hash and s_hash[s_char] != t_char or t_char in t_hash and t_hash[t_char] != s_char:
                    return False
        return True
                
        

            
        
        
        


                
                
            
            
        