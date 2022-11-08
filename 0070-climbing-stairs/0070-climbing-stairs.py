class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i >= n:
                return 1
            
            return dp(i+1) + dp(i+2) 
        
        return dp(1)    
        
#         def dp(i):
#             if i >= n:
#                 return 1
            
#             if i in memo:
#                 return memo[i]
            
#             memo[i] = dp(i+1) + dp(i+2) 
#             return memo[i]
        
#         memo = {}
#         return dp(1)
            