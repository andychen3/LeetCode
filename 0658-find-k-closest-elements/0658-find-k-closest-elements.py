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
        
        while heap:
            heapq.heappush(second_heap, -heapq.heappop(heap)[1])
        
        ans = []

        while second_heap:
            ans.append(heapq.heappop(second_heap))
        return ans