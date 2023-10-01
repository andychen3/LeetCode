import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        hash_set = set(nums)
        heap = [-num for num in hash_set]
        heapify(heap)
        last = 0
        i = 0

        while heap and i < 3:
            last = heapq.heappop(heap)
            i += 1
        return -last if i == 3 else max(nums)