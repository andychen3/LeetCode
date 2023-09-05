class Solution:
    def maximum69Number (self, num: int) -> int:
        converted = [digit for digit in str(num)]
        

        for index, digits in enumerate(converted):
            if digits == '6':
                converted[index] = '9'
                break
        
        return int("".join(converted))

        

        