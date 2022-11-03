import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)
        
        while len(sticks) > 1:
            stick_1 = heapq.heappop(sticks)
            stick_2 = heapq.heappop(sticks)
            combined_cost = stick_1+stick_2
            cost += combined_cost
            heapq.heappush(sticks, combined_cost)
        return cost
        