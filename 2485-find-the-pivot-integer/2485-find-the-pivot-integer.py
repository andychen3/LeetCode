class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        right = n
        left_sum = left
        right_sum = right
        
        if n == 1:
            return 1
        
        while left < right:
            if left_sum < right_sum:
                left += 1
                left_sum += left
            else:
                right -= 1
                right_sum += right
                
            if left_sum == right_sum and left + 1 == right - 1:
                return left + 1
        return -1
                