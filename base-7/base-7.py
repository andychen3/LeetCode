class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        res = []
        signed = False
        if num < 0:
            signed = True
        num = abs(num)
            
        while num:
            num, remainder = divmod(num, 7)
            res.append(str(remainder))
        
        if signed:
            res.append("-")
        
        return "".join(reversed(res))