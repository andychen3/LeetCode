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
        # This approach is still slow, but is better than my other approach because sorting is klogk and not nlogn since we only are sorting k elements. 
        return sorted([-num[1] for num in heap])