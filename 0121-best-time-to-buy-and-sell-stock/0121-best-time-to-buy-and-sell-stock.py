class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        
        for price in prices:
            
            while price < prices[left]:
                left += 1
            
            profit = max(profit, price - prices[left])
        
        return profit