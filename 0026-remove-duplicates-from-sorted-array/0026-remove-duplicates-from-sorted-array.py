class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1 #This is where to insert the next unique element
        
        for right in range(1, len(nums)):
            if nums[index-1] != nums[right]:
                nums[index] = nums[right]
                index += 1
        return index