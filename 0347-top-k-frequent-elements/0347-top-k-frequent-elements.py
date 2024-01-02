from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums).most_common()
        arr = []
        
        
        for i in range(k):
            arr.append(counts[i][0])

        return arr
            