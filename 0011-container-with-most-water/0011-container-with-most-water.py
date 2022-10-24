class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0 , len(height)-1
        
        while left < right:
            left_height = height[left]
            right_height = height[right]
            area = max(area, min(left_height,right_height)*(right-left))
            if left_height < right_height:
                left += 1
            else:
                right -= 1
            
        return area
        
        