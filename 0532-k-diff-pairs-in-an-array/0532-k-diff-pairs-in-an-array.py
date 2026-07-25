from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        count = 0

        if k == 0:
            for num in freq.values():
                if num >= 2:
                    count += 1
        else:
            for num in freq:
                if num + k in freq:
                    count += 1
        return count