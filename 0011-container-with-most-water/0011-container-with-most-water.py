class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        
        while left < right:
            min_height = min(height[left], height[right])
            ans = max(ans, min_height*(right-left))
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans