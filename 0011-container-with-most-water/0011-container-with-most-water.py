class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height)-1
        
        while left < right:
            left_num = height[left]
            right_num = height[right]
            
            max_water = max(max_water, min(left_num, right_num)*(right-left))
            
            if left_num < right_num:
                left += 1
            else:
                right -= 1
        return max_water