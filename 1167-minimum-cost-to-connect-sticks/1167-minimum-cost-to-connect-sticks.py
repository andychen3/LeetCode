import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        
        while len(sticks) > 1:
            first_stick = heappop(sticks)
            second_stick = heappop(sticks)
            
            cost += first_stick + second_stick
            heappush(sticks, first_stick + second_stick)
        
        return cost