class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        insert_index = 1
        for i in range(1, N):
            if nums[i-1] != nums[i]:
                nums[insert_index] = nums[i]
                insert_index += 1
        return insert_index