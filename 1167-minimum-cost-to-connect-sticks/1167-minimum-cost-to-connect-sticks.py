import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) < 2:
            return 0
        
        heapq.heapify(sticks)
        ans = 0
        
        while len(sticks) > 1:
            first_stick = heapq.heappop(sticks)
            second_stick = heapq.heappop(sticks)
            combined_stick = first_stick+second_stick
            ans += combined_stick
            heapq.heappush(sticks, combined_stick)
            
        return ans
            
            
            