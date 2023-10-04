from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        freq = sorted(counts.values(), reverse=True)[k-1]

        ans = []

        for num in counts:
            if counts[num] >= freq:
                ans.append(num)
        return ans