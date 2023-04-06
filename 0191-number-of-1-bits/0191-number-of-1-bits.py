class Solution:
    def hammingWeight(self, n: int) -> int:
        
        xor = 0 ^ n
        ans = 0
        while xor:
            if xor & 1:
                ans += 1
            xor >>= 1
        return ans