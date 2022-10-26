class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        res = 0
        
        for rocks in stones:
            if rocks in jewels_set:
                res += 1
        return res


        
            
        