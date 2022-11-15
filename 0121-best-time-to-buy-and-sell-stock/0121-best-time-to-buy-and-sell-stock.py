class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window_start, profit = 0, 0
        
        for window_end in range(len(prices)):
            if prices[window_end] < prices[window_start]:
                window_start = window_end
        
            profit = max(profit, prices[window_end]-prices[window_start])
            
        return profit
            