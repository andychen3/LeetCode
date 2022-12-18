class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        i = 0
        
        for temps in temperatures:
            while len(stack) > 0 and stack[-1][0] < temps:
                temp, index = stack.pop()
                ans[index] = i-index
                
            stack.append((temps, i))
            i += 1
            
        return ans

        