class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices.copy()
        
        for index, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                prev_price, idx = stack.pop()
                ans[idx] = prev_price - price
            
            stack.append([price, index])
        return ans