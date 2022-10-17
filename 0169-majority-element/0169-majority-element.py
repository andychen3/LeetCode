class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = collections.Counter(nums)
        sorted_hash = sorted(hash.items(), key=lambda x:x[1], reverse=True)
        return sorted_hash[0][0]
        