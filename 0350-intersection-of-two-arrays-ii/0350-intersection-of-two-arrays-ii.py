class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_hash = collections.Counter(nums1)
        res = []
        
        for num in nums2:
            if num in nums1_hash and nums1_hash[num] != 0:
                nums1_hash[num] -= 1
                res.append(num)
        return res
                