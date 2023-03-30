import heapq
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        ans = 0
        money = 0
        
        while money < coins and len(costs) != 0:
            cost = heapq.heappop(costs)
            if money + cost <= coins:
                money += cost
                ans += 1
        
        return ans
            
                
            