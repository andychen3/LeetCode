from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        ans = []

        for key, val in freq.items():
            if val > n/3:
                ans.append(key)
        return ans