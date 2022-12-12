class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        def dfs(steps):
            if steps <= 2:
                return steps
            
            if steps in memo:
                return memo[steps]
            
            memo[steps] = dfs(steps-1)+dfs(steps-2)
            return memo[steps]
        
        return dfs(n)
        