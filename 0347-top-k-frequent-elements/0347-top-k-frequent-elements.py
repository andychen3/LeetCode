from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        freq = sorted(counts.values(), reverse=True)[k-1]

        res = []
        for key, val in counts.items():
            if val >= freq:
                res.append(key)
        return res