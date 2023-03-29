import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-rock for rock in stones]
        heapq.heapify(stone)
        
        while len(stone) > 1:
            first_rock = abs(heapq.heappop(stone))
            second_rock = abs(heapq.heappop(stone))
            
            if first_rock != second_rock:
                heapq.heappush(stone, -abs(first_rock-second_rock))
        return -stone[0] if stone else 0
            