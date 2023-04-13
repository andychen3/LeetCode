class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights = [0] + heights + [0]
        
        for i, h in enumerate(heights):
            while stack and stack[-1][1] > h:
                height = stack.pop()[1]
                width = i - stack[-1][0] - 1
                max_area = max(max_area, height*width)
            stack.append((i, h))
        return max_area