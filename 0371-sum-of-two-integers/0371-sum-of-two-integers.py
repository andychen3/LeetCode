class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        
        while b != 0:
            temp = (a&b) << 1 # finds the carry
            a = (a^b) & mask # a^b is the addition without carry and we AND to mask to prevetn overflow
            b = temp & mask # same here we AND it to prevent overflow
            
        if a > mask // 2:
            return ~(a^mask)
        else:
            return a