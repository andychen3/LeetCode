class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []
        negative = False
        if num < 0:
            negative = True
            num = abs(num)
        
        while num:
            quotient, remainder = divmod(num, 7)
            res.append(str(remainder))
            num = quotient

        if negative:
            res.append("-")
        ans = "".join(reversed(res))
        return ans