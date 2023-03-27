class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                latest_index, latest_temp  = stack.pop()
                ans[latest_index] = index - latest_index
            
            stack.append([index, temp])
        return ans