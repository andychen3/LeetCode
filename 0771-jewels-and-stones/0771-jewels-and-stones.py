class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        
        for rock in stones:
            if rock in jewels:
                res += 1
                
        return res

        
            
        