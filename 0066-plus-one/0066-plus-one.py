class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) -1, -1, -1):
            if digits[i] == 9:
                carry = 1
                digits[i] = 0
                continue
            else:
                if carry:
                    digits[i] += 1
                    return digits
                digits[i] += 1
                return digits
        return [1] + digits
                
            