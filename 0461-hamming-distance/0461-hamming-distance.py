class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        xor = x ^ y
        
        while xor:
            xor = xor & (xor-1)
            res += 1
            
        
        return res