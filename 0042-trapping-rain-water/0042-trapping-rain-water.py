class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        
        max_left = height[0]
        max_right = height[right]
        ans = 0
        
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                ans += max_left- height[left]
                
            else:
                right -= 1
                max_right = max(max_right, height[right])
                ans += max_right - height[right]
                
        return ans