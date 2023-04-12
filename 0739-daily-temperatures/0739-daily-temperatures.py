class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        
        for index, temps in enumerate(temperatures):
            while stack and stack[-1][1] < temps:
                idx, temp = stack.pop()
                ans[idx] = index-idx
                
            stack.append([index, temps])
        return ans
            
            
        

                    
            