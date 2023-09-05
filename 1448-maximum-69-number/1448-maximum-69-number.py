class Solution:
    def maximum69Number (self, num: int) -> int:
        # converted = [digit for digit in str(num)]
        # easier way to conver to a list is to do list(str(num))
        converted = list(str(num))
        

        for index, digits in enumerate(converted):
            if digits == '6':
                converted[index] = '9'
                break
        
        return int("".join(converted))

        

        