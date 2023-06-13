class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        size = len(nums)
        count = nums.count(target)
        
        return count > (size / 2)