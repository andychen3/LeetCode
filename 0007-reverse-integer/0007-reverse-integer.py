class Solution:
    def reverse(self, x: int) -> int:
        max_int = pow(2,31) - 1
        min_int = pow(-2,31)
        
        str_x = str(abs(x))
        reverse_str = str_x[::-1]
        result = int(reverse_str)
        result = result* -1 if x < 0 else result
        
        return result if (result < max_int and result > min_int) else 0