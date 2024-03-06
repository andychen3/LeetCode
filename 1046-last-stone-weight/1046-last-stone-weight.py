import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-i for i in stones]
        heapify(stone)
        
        while len(stone) > 1:
            first = heappop(stone)
            second = heappop(stone)
            
            if first != second:
                heappush(stone, first - second)
        return -stone[0] if stone else 0