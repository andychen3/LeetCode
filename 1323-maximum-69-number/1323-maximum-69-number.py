class Solution:
    def maximum69Number (self, num: int) -> int:
        new = list(str(num))
        
        for index, n in enumerate(new):
            if n == '6':
                new[index] = '9'
                break
        
        return int("".join(new))