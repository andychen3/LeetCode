class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                ans[idx] = index-idx
            stack.append(index)
        return ans