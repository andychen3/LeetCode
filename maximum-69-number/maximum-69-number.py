class Solution:
    def maximum69Number (self, num: int) -> int:
        string_num = list(str(num))
        
        for index, digits in enumerate(string_num):
            if digits == '6':
                string_num[index] = '9'
                break
        return int("".join(string_num))