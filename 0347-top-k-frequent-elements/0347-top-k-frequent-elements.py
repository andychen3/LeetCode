class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = collections.Counter(nums)
        res = [x[0] for x in hash.most_common(k)]
        return res
  
        