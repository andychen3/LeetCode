import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-rocks for rocks in stones]
        heapify(stone)
        
        while len(stone) > 1:
            first_stone = heappop(stone)
            second_stone = heappop(stone)
            
            if first_stone != second_stone:
                heappush(stone, first_stone - second_stone)
        return -stone[0] if stone else 0