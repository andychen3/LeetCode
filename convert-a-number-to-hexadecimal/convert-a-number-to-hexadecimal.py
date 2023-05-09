class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        mappings = '0123456789abcdef'
        res = []
        for i in range(8):
            num, remainder = divmod(num, 16)
            res.append(str(mappings[remainder]))
        return "".join(res[::-1]).lstrip("0")