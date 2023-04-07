class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        
        while left < right:
            left_num = numbers[left]
            right_num = numbers[right]
            
            if left_num + right_num == target:
                return [left+1, right+1]
            
            if left_num + right_num > target:
                right -= 1
            else:
                left += 1
        
        return -1
            