class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        
        for i, h in enumerate(chain([0]+heights+[0])):
            while stack and stack[-1][1] > h:
                prev_height = stack.pop()[1]
                width = i - stack[-1][0] - 1
                max_area = max(max_area, prev_height*width)
            stack.append((i, h))
        return max_area