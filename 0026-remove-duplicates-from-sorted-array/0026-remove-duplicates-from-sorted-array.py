class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_index = 1

        for i in range(1, len(nums)):
            # We are using 3 pointers. Insert_index is the place to add the correct num
            # i as the one to check the next nums and i-1 to compare if the previous is a different num
            
            if nums[i] != nums[i-1]:
                nums[insert_index] = nums[i]
                insert_index += 1

        return insert_index