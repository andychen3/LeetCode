class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices.copy()
        
        for index, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                ans[idx] -= price
            
            stack.append(index)
        return ans