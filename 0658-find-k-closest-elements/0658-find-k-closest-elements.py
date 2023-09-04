import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        second_heap = []

        for num in arr:
            # I am creating a max heap so i can get rid of the furthest elements from x
            heapq.heappush(heap, (-abs(num-x), -num))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return sorted([-num[1] for num in heap])