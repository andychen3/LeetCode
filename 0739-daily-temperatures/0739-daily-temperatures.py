class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        
        for index in range(len(temperatures)):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                last_temp = stack.pop()
                ans[last_temp] = index-last_temp
            stack.append(index)
        return ans
        